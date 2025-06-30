import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API Key
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Initialize Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# UI Design
st.set_page_config(page_title="AI Study Buddy Chatbot", page_icon="🤖")
st.title("🤖 My AI Study Buddy Chatbot")
st.caption("Your personal AI-powered math & science tutor!")

# Sidebar for Subject Selection
subject = st.sidebar.selectbox("Choose a subject 📚", ["General", "Math", "Science"])

# Display Chat History
for entry in st.session_state.chat_history:
    role, message = entry
    if role == "user":
        st.chat_message("user").markdown(message)
    else:
        st.chat_message("assistant").markdown(message)

# User Input
user_input = st.chat_input("Ask me a question...")

# Generate AI Response
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤖"):
            try:
                prompt = f"Answer this {subject.lower()} question: {user_input}"
                response = model.generate_content(prompt)
                reply = response.text.strip()
                st.markdown(reply)
                st.session_state.chat_history.append(("bot", reply))
            except Exception as e:
                error_message = f"Error: {e}"
                st.error(error_message)
                st.session_state.chat_history.append(("bot", error_message))