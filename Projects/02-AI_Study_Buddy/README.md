# AI Study Buddy Chatbot

## Table of Contents
- [🛠️ Prerequisites](#prerequisites)
- [⚙️ Setup](#setup)
- [🔑 .env & Environment Variables](#env--environment-variables)
- [💬 Usage](#usage)
- [📁 File Structure](#file-structure)
- [🧑‍💻 Code Explainer](#code-explainer)
- [✨ Further Enhancements](#further-enhancements)

An intelligent AI-powered chatbot designed to help students with their studies, featuring both basic and advanced versions with subject-specific tutoring capabilities.

## Setup

1. Install dependencies:
```bash
pip install streamlit google-generativeai python-dotenv
```

2. Create `.env` file:
```bash
# Copy the template file and rename it to .env
cp env_template.txt .env
# Edit .env and add your actual Gemini API key
```

3. Run the application:
```bash
# For basic version
streamlit run basic.py

# For advanced version
streamlit run advanced.py
```

## .env & Environment Variables

This project uses a `.env` file to securely store your Google Gemini API key. The `.env` file should be placed in the same directory as your code.

**Example `.env` file:**
```env
GEMINI_API_KEY=your-actual-gemini-api-key-here
```

- Never share your `.env` file or commit it to version control (e.g., GitHub).
- Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

### Loading Environment Variables in Python

This project uses the [`python-dotenv`](https://pypi.org/project/python-dotenv/) package to load environment variables from the `.env` file automatically. In both `basic.py` and `advanced.py`, the following code loads your variables:

```python
from dotenv import load_dotenv
load_dotenv()
```

You can then access your API key using:

```python
import os
api_key = os.getenv('GEMINI_API_KEY')
```

## Usage

### Basic Version (`basic.py`)
1. Open your web browser and navigate to the Streamlit app
2. Select a subject from the sidebar (General, Math, or Science)
3. Type your question in the chat input at the bottom
4. Press Enter to get an AI response
5. The conversation history is maintained throughout your session

### Advanced Version (`advanced.py`)
1. Open your web browser and navigate to the Streamlit app
2. Select a subject from the sidebar (General, Math, or Science)
3. Optionally enable "Explain Like I'm 5" mode for simpler explanations
4. Type your question in the chat input
5. The AI will provide context-aware responses based on your conversation history

## 🛠️ Prerequisites

- Python 3.8 or higher
- A Google account and Gemini API key ([get yours here](https://makersuite.google.com/app/apikey))
- Internet connection

## 📁 File Structure

- `basic.py` — Basic version of the AI Study Buddy with simple chat functionality
- `advanced.py` — Advanced version with ELI5 mode and conversation context awareness
- `requirements.txt` — Python dependencies
- `env_template.txt` — Template for environment variables (copy to `.env` and add your API keys)
- `README.md` — Project documentation (this file)

## 🧑‍💻 Code Explainer

This project features two versions of an AI-powered study assistant:

### Basic Version (`basic.py`)
- **Simple Chat Interface**: Clean, straightforward chat interface using Streamlit
- **Subject Selection**: Choose from General, Math, or Science subjects
- **Session Management**: Maintains chat history using Streamlit's session state
- **Error Handling**: Graceful error handling with user-friendly messages

### Advanced Version (`advanced.py`)
- **Enhanced Features**: All basic features plus additional capabilities
- **ELI5 Mode**: "Explain Like I'm 5" toggle for simplified explanations
- **Context Awareness**: Uses conversation history to provide more relevant responses
- **Improved Prompts**: Better prompt engineering for subject-specific responses

### Key Components:
1. **Environment Setup**: Loads Gemini API key from `.env` file
2. **Gemini Integration**: Uses `gemini-1.5-flash` model for responses
3. **Streamlit UI**: Modern, responsive web interface with chat bubbles
4. **Session State**: Maintains conversation history across interactions
5. **Error Handling**: Robust error handling with user feedback

✨ Perfect for students who need help with homework, exam preparation, or general learning! 📚

## ✨ Further Enhancements

Want to take this project further? Here are some ideas:

- 📊 **Progress Tracking**: Add features to track learning progress over time
- 🎯 **Practice Quizzes**: Generate interactive quizzes based on subjects
- 📝 **Note Taking**: Allow students to save important explanations
- 🎨 **Visual Learning**: Add support for diagrams and visual explanations
- 🔍 **Search History**: Add ability to search through previous conversations
- 📱 **Mobile App**: Convert to a mobile application
- 🌍 **Multi-language**: Add support for multiple languages
- 🎓 **Grade-specific Content**: Tailor responses to specific grade levels
- 📚 **Resource Links**: Provide links to additional learning resources
- 🤝 **Collaborative Learning**: Add features for group study sessions

Feel free to experiment and make it your own! 🚀 