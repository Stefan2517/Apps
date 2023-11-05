import streamlit as st
from PIL import Image #trebuie aici pillow instalat
#streamlit run Web_camera.py

with st.expander("Porneste camera web"):
    #Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    #Create a pillow image instances
    img = Image.open(camera_image)

    #Convert the pillow image to grayscale
    gray_img = img.convert("L")

    #Render the grayscale image on the webpage
    st.image(gray_img)
