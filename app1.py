import os
import streamlit as st
import google.generativeai as genai
from api_key import api_key
from PIL import Image

# Configure Gemini AI with API key
genai.configure(api_key=api_key)

# Set the model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Load the model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",  # Updated to the latest Gemini model
    generation_config=generation_config,
)

# Streamlit UI
st.set_page_config(page_title="Img Analytics", page_icon="🤖")
st.title("📸 Vital Image Analytics 🔍")
st.subheader("An application that helps users identify medical images.")

# File uploader
uploaded_file = st.file_uploader("Upload a medical image for analysis", type=["png", "jpg", "jpeg"])

# Button to generate analysis
if st.button("Generate the analysis"):
    if uploaded_file is not None:
        # Open the image using PIL
        image = Image.open(uploaded_file)

        # Display uploaded image
        st.image(uploaded_file, use_container_width=True)


        # Send request to Gemini with PIL Image
        response = model.generate_content([image, "Describe the medical aspects of this image."])

        # Display the AI-generated response
        st.write("### Analysis Result:")
        st.write(response.text)
    else:
        st.warning("Please upload an image before generating analysis.")
