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
if "eli5_mode" not in st.session_state:
    st.session_state.eli5_mode = False

# UI Design
st.set_page_config(page_title="AI Study Buddy Chatbot", page_icon="🤖")
st.title("🤖 My AI Study Buddy Chatbot")
st.caption("Your personal AI-powered math & science tutor!")

# Sidebar for Subject Selection and ELI5 Mode Toggle
subject = st.sidebar.selectbox("Choose a subject 📚", ["General", "Math", "Science"])
st.session_state.eli5_mode = st.sidebar.checkbox("Explain Like I'm 5 (ELI5) 🧒", st.session_state.eli5_mode)

# Display Chat History
for entry in st.session_state.chat_history:
    role, message = entry
    if role == "user":
        st.chat_message("user").markdown(message)
    else:
        st.chat_message("assistant").markdown(message)

# User Input
user_input = st.chat_input("Ask me a question...")

# Generate AI Response with Context Awareness and ELI5 Mode
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤖"):
            try:
                # Building conversation context
                context = "\n".join([f"{role}: {msg}" for role, msg in st.session_state.chat_history[-5:]])  # Last 5 interactions
                eli5_prefix = "Explain like I'm 5: " if st.session_state.eli5_mode else ""
                prompt = f"{context}\n{eli5_prefix}Answer this {subject.lower()} question: {user_input}"
                response = model.generate_content(prompt)
                reply = response.text.strip()
                st.markdown(reply)
                st.session_state.chat_history.append(("assistant", reply))
            except Exception as e:
                error_message = f"Error: {e}"
                st.error(error_message)
                st.session_state.chat_history.append(("assistant", error_message))