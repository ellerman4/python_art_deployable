import cv2
import numpy as np
from scipy.spatial import Delaunay
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter, ImageEnhance


# Get user input
with st.sidebar:
    st.header('Art with Triangulation!')

    lower_thresh = st.slider('Lower Threshold', 0, 200, 40)
    upper_thresh = st.slider('Upper Threshold', 0, 200, 120)
    tri_line_width= st.slider('Line Thickness', 0.1, 2.0, .3)
    black_white = st.sidebar.checkbox("Black and white (breaks transparency)")

    options_col_1, optons_col_2 = st.sidebar.columns(2)
    with options_col_1:
        flip_x = st.checkbox("Flip X")
        color1 = st.color_picker('Pick A Color', '#FF0076')
    with optons_col_2:
        flip_y = st.checkbox("Flip Y")
        color2 = st.color_picker('Pick A Color', '#590FB7')


    gradient_cb = st.sidebar.checkbox("Apply gradient")

    img_file_buffer = st.file_uploader("Upload an image")
    if img_file_buffer is not None:
        image = Image.open(img_file_buffer)
        img = np.array(image) # if you want to pass it to OpenCV


if img_file_buffer:

    # Convert to graycsale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 

    # Canny Edge Detection
    edges = cv2.Canny(image=img_blur, threshold1=lower_thresh, threshold2=upper_thresh) # Adjust threshold variables for desired result
    imS = cv2.resize(edges, (900,720))

    # Find contours of canny edge detection image
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Get points from the countour map
    points = np.vstack(contours).squeeze()

    # Create Delaunay triangulation from points
    tri = Delaunay(points).simplices.copy()

    # Color mapping
    centers = np.sum(points[tri], axis=1, dtype='int')/3.0
    colors = np.array([ (x/2.)**2 + (y/2.)**2 for x,y in centers])

    # Plot colored Delaunay triangulation
    fig = plt.tripcolor(points[:,0], points[:,1], tri, facecolors=colors, edgecolors='k')
    fig.set_linewidth(tri_line_width)

    # Flip the image, (not sure why points are inverted)
    plt.gca().invert_yaxis()
    plt.axis('off')


    # Save fig as image file with transparent background, display the image
    plt.savefig("./output/test.png", dpi = 600, transparent=True)

    st.header('Delaunay Triangulation Image 📸')    # Write header with cute emoji 📸
    mutable_img = Image.open("./output/test.png")   # Open the saved figure 

    # Options for image modifications
    if black_white:
        mutable_img = mutable_img.convert(mode='L')

    if flip_y:
        mutable_img = mutable_img.transpose(Image.FLIP_TOP_BOTTOM)
    elif flip_x:
        mutable_img = mutable_img.transpose(Image.FLIP_LEFT_RIGHT)



    # Display the final image
    st.image(mutable_img)

    # Custom css for gradient background colors
    if gradient_cb:
        st.markdown(
            f'<style> .css-1v0mbdj {{ background-image: linear-gradient({color1}, {color2}); }} </style>',
            unsafe_allow_html=True
            )

    # Custom css for gradient hue
    hue = st.slider('Hue', 0, 360, 0)
    st.markdown(
            f'<style> .etr89bj1 {{ filter: hue-rotate({hue}deg); }} </style>',
            unsafe_allow_html=True
            )

    # Display Canny Edge Detection Image
    st.header('Edge Detection Image')
    st.markdown('Adjust threshold variables for desired output')
    st.image(imS)