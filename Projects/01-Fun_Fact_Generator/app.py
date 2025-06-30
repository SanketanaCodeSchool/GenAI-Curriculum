import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to generate a fun fact
def generate_fun_fact(topic):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Tell me a fun fact about {topic}.")
    return response.text.strip()

# Streamlit UI
st.title("🎉 AI-Powered Fun Facts Generator")
st.write("Enter a topic, and the AI will generate a fun fact for you!")

topic = st.text_input("Enter a topic (e.g., Space, Animals, History)")

if st.button("Generate Fun Fact"):
    if topic:
        fact = generate_fun_fact(topic)
        st.success(fact)
    else:
        st.warning("Please enter a topic.")