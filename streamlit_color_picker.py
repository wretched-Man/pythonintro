# Use 3 sliders that run from 0 - 255 for RGB
# on selecting, show the value chosen and the 
# color in a 256 * 256 box
import cv2
import numpy as np
import streamlit as st

#Our function to build a 3-channel image
def display_col(color_tuple : tuple, shape = (512, 512, 3)):
    '''
    Given an RGB tuple, return a 3-channel 
    numpy array as RGB. The last axis of shape must
    be equal to the length of color_tuple.
    '''

    #asserting the above
    assert(len(color_tuple) == shape[2])

    color_img = np.zeros(shape, np.uint8)
    
    color_img[:, :, 0] = color_tuple[0]
    color_img[:, :, 1] = color_tuple[1]
    color_img[:, :, 2] = color_tuple[2]
    return color_img

st.header("Color Picker")
st.write('''
This is a simple implementation of a color picker. 
Adjust the values for R, G and B and get a display 
of the color represented.
''')

# Separate section
st.write('---')

color_slider, color_view = st.columns((1, 2))

#We will need the slider values
red_slider = 0
green_slider = 0
blue_slider = 0

# Slider
with color_slider:
    st.subheader("Pick Color")
    st.write("""
Slide the various bars to adjust the RGB values.
 The resultant color is displayed on the right.
""")
    
    red_slider = st.slider('Red', 0, 255, 128)
    green_slider = st.slider('Green', 0, 255, 128)
    blue_slider = st.slider('B:ue', 0, 255, 128)
    st.write('##')

with color_view:
    st.markdown("<h2 style='text-align: center;"
                "color: white;'>Color</h2>",
                unsafe_allow_html=True)
    #st.write('###')
    st.write('RGB: ', red_slider, green_slider, blue_slider)

    #Picked from the left column
    color_tuple = (red_slider, green_slider, blue_slider)

    st.image(display_col(color_tuple))

