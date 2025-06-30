import streamlit as st
import openai
import os
from dotenv import load_dotenv
from PIL import Image
import base64
from io import BytesIO
import requests
from huggingface_hub import InferenceClient
import time
import httpx
import sys


# Load environment variables
load_dotenv()

# Configure OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configure Hugging Face
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
client = InferenceClient(token=HF_TOKEN)

# Set page config
st.set_page_config(
    page_title="AI Storybook Creator",
    page_icon="📚",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .story-text {
        font-size: 18px;
        line-height: 1.6;
        margin-bottom: 20px;
    }
    .story-image {
        max-width: 100%;
        height: auto;
        border-radius: 10px;
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

def generate_story(prompt, age_group):
    """Generate a story using OpenAI"""
    system_prompt = f"""Create a short, engaging story suitable for {age_group} students. 
    The story should be educational, fun, and include a moral lesson. 
    Make it approximately 300 words long."""
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500
    )
    
    return response.choices[0].message.content

def generate_image(prompt):
    """Generate an image using Hugging Face's Stable Diffusion"""
    try:
        # Using Stable Diffusion XL model
        API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
        headers = {"Authorization": f"Bearer {HF_TOKEN}"}
        
        # Prepare the prompt for child-friendly illustration
        enhanced_prompt = f"children's book illustration style, {prompt}, colorful, friendly, safe for children, high quality, detailed, digital art, cute, whimsical, masterpiece, best quality"
        
        # Add retry mechanism
        max_retries = 3
        for attempt in range(max_retries):
            try:
                # Make the API request
                response = requests.post(API_URL, headers=headers, json={"inputs": enhanced_prompt})
                
                if response.status_code == 200:
                    # Convert the image bytes to base64
                    image_bytes = response.content
                    img_str = base64.b64encode(image_bytes).decode()
                    return f"data:image/jpeg;base64,{img_str}"
                elif response.status_code == 503:
                    # Model is loading, wait and retry
                    if attempt < max_retries - 1:
                        st.info("Model is loading, please wait...")
                        time.sleep(5)  # Wait 5 seconds before retrying
                        continue
                else:
                    st.error(f"Error from Hugging Face API: {response.status_code}")
                    st.error(f"Response content: {response.text}")
                    return "https://via.placeholder.com/400x300?text=Image+Generation+Failed"
            except Exception as e:
                if attempt < max_retries - 1:
                    st.warning(f"Attempt {attempt + 1} failed, retrying...")
                    time.sleep(2)
                    continue
                else:
                    st.error(f"Error generating image: {str(e)}")
                    return "https://via.placeholder.com/400x300?text=Image+Generation+Failed"
            
    except Exception as e:
        st.error(f"Error generating image: {str(e)}")
        return "https://via.placeholder.com/400x300?text=Image+Generation+Failed"

def main():
    st.title("📚 AI Storybook Creator")
    st.write("Create personalized stories with AI-generated illustrations!")

    
    # Input section
    col1, col2 = st.columns(2)
    
    with col1:
        story_prompt = st.text_area(
            "What would you like your story to be about?",
            placeholder="Example: A magical garden where plants can talk"
        )
    
    with col2:
        age_group = st.selectbox(
            "Select age group",
            ["Elementary (6-10)", "Middle School (11-13)", "High School (14-18)"]
        )
    
    if st.button("Generate Story"):
        if story_prompt:
            with st.spinner("Creating your story..."):
                # Generate story
                story = generate_story(story_prompt, age_group)
                
                # Split story into paragraphs
                paragraphs = story.split('\n\n')
                
                # Generate image for the first paragraph
                image_prompt = f"children's book illustration for: {paragraphs[0][:100]}"
                image_data = generate_image(image_prompt)
                
                # Display story with image
                st.markdown("### Your Story")
                st.markdown(f'<img src="{image_data}" class="story-image">', unsafe_allow_html=True)
                
                for paragraph in paragraphs:
                    st.markdown(f'<p class="story-text">{paragraph}</p>', unsafe_allow_html=True)
                
                # Add download button
                st.markdown("### Download Your Story")
                html_content = f"""
                <html>
                <head>
                    <style>
                        body {{ font-family: Arial, sans-serif; margin: 40px; }}
                        .story-text {{ font-size: 18px; line-height: 1.6; margin-bottom: 20px; }}
                        .story-image {{ max-width: 100%; height: auto; border-radius: 10px; margin: 20px 0; }}
                    </style>
                </head>
                <body>
                    <h1>My AI Story</h1>
                    <img src="{image_data}" class="story-image">
                    {''.join(f'<p class="story-text">{p}</p>' for p in paragraphs)}
                </body>
                </html>
                """
                
                b64 = base64.b64encode(html_content.encode()).decode()
                href = f'<a href="data:text/html;base64,{b64}" download="my_story.html">Download Story as HTML</a>'
                st.markdown(href, unsafe_allow_html=True)
        else:
            st.warning("Please enter a story prompt!")

if __name__ == "__main__":
    main() 