# Given an image, show the resultant mask produced when it
# undergoes binary thresholding

import sys
import cv2
import streamlit as st
import numpy as np

#Define a function that returns a mask, given an image
def gen_mask(img, threshold_type: str, thresh_value):
    #The image must be grayscale
    assert(len(img.shape) == 2)

    #This is what will be returned
    mask = np.empty((img.shape[0], img.shape[1]), np.uint8)

    if threshold_type == 'THRESH_BINARY':
        _, mask = cv2.threshold(img, thresh_value, 255,\
                                cv2.THRESH_BINARY)
    elif threshold_type == 'THRESH_BINARY_INV':
        _, mask = cv2.threshold(img, thresh_value, 255,\
                                cv2.THRESH_BINARY_INV)
    else:
        st.error(
            "An incorrect option was chosen. Will likely"
            " return random bytes."
        )
    return mask


st.header('Display Mask')

#Ask the user for an image
file = st.file_uploader(
    "Input an image file!",
    ["png", "jpg", "jpeg", "bmp"]
)

# The rest of the processes only happen 
# if there is a file to process
if file is not None:
    #convert file to acceptable input for opencv
    file_bytes = np.asarray(bytearray(file.read()), np.uint8)
    img = cv2.imdecode(file_bytes, cv2.IMREAD_UNCHANGED)

    #Convert to gray
    img_gray = np.empty((img.shape[0], img.shape[1]), np.uint8)
    
    #if 1 channel
    if len(img.shape) == 2:
        img_gray = img.copy()
    else:
        if img.shape[2] == 3:
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        elif img.shape[2] == 4:
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        else:
            st.error(
                "The Image file could not be processed."
            )
            sys.exit()

    image_col, mask_col = st.columns(2)

    with image_col:
        st.subheader('Image')
        st.write('#')
        st.write('#')
        st.write('#')
        st.image(img,
                 caption='Original | ' + file.name,
                 )

    with mask_col:

        threshold_value = 0
        threshold_type = ''

        st.subheader('Mask')
        threshold_type = st.selectbox(
            "Choose a threshold type.",
            ['THRESH_BINARY', 'THRESH_BINARY_INV'],
            index = 1
        )

        threshold_value = st.slider(
            "Choose a threshold value.",
            0, 255, 127
        )

        #produce the mask
        mask = gen_mask(img_gray, threshold_type, threshold_value)

        st.write('###')
        st.image(mask,
                 caption = 'Mask | ' + 
                 threshold_type + ' | ' +
                    str(threshold_value))
else:
    st.write(
        "Waiting for file..."
    )

                 



