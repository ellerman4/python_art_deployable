import streamlit as st

# Simple fade in animation for image
def fade_in():
    st.markdown(
    """
    <style>
    .etr89bj1 {
        animation: fade-in 1.2s cubic-bezier(0.390, 0.575, 0.565, 1.000) both;
    }
    @keyframes fade-in {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
    )


# Some simple icons for social media
def footer_icons():
    st.markdown(
    """
    <style>
    @import url('//maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css');

    a, a:hover {
        text-decoration: none;
    }

    .socialbtns, .socialbtns ul, .socialbtns li {
        margin: 0;
        padding: 5px;
    }

    .socialbtns li {
        list-style: none outside none;
        display: inline-block;
    }

    .socialbtns .fa {
        width: 40px;
        height: 28px;
        color: #fff;
        background-color: #000;
        border: 1px solid #ffffff;
        padding-top: 6px;
        border-radius: 22px;
        -moz-border-radius: 22px;
        -webkit-border-radius: 22px;
        -o-border-radius: 22px;
    }

    .socialbtns .fa:hover {
        color: #000;
        background-color: #ffffff;
        border: 1px solid #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    st.markdown(
    """
    <div align="center" class="socialbtns">
        <ul>
            <li><a href="https://github.com/ellerman4" class="fa fa-lg fa-github"></a></li>
            <li><a href="https://twitter.com/" class="fa fa-lg fa-twitter"></a></li>
            <li><a href="https://www.linkedin.com/" class="fa fa-lg fa-linkedin"></a></li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
    )
