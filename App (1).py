import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image
import datetime

client = InferenceClient(token=os.genenv(HF_TOKEN))

MODEL = "stabilityai/stable-diffusion-xl-base-1.0"

st.set_page_config(page_title="My Image Generator")

st.write("Describe your imagination to make it real..")

prompt = st.text_input("Describe your image..")

if st.button("Generate"):
    if prompt.strip() == "":
        st.warning("Please enter a prompt first!")
    else:
        with st.spinner("Image is creating..."):
            image = client.text_to_image(prompt, model=MODEL)

            st.image(image, caption=prompt)

            image.save("myimage.png")

            st.success("Image saved in current working directory")