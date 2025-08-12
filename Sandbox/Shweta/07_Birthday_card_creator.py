import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI
from PIL import Image
import requests
from io import BytesIO

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# Set up OpenAI client
client = OpenAI(api_key=API_KEY)

# Streamlit UI
st.title("🎂 AI Birthday Card Creator")
st.markdown("Describe what you want on your birthday card, and let AI generate the image!")

# User input prompt
user_prompt = st.text_input("What should the card show?", 
                            placeholder="e.g. A cute cat holding balloons in a garden")

# Button to generate image
if st.button("Generate Birthday Card"):
    if user_prompt.strip() == "":
        st.warning("Please enter a description first.")
    else:
        with st.spinner("Creating your AI birthday card..."):
            try:
                # Generate image using DALL·E
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=user_prompt,
                    size="1024x1024",
                    quality="standard",
                    n=1,
                )
                image_url = response.data[0].url
                #st.write(image_url)

                # Display image
                st.image(image_url, caption="Your AI-generated birthday card 🎉", use_column_width=True)

                # Download option
                img_data = requests.get(image_url).content
                st.download_button("Download Image", img_data, "birthday_card.png", "image/png")

            except Exception as e:
                st.error(f"Something went wrong: {e}")
