# AI-Powered Fun Facts Generator

## Table of Contents
- [🛠️ Prerequisites](#prerequisites)
- [⚙️ Setup](#setup)
- [🔑 .env & Environment Variables](#env--environment-variables)
- [💬 Usage](#usage)
- [📁 File Structure](#file-structure)
- [🧑‍💻 Code Explainer](#code-explainer)
- [✨ Further Enhancements](#further-enhancements)

An interactive web application that generates fun facts about any topic using Google's Gemini AI model.

## Setup

1. Install dependencies:
```bash
pip install streamlit google-generativeai python-dotenv
```

2. Create `.env` file:
```bash
# Create .env file and add your Gemini API key
GEMINI_API_KEY=your-gemini-api-key-here
```

3. Run the application:
```bash
streamlit run app.py
```

## .env & Environment Variables

This project uses a `.env` file to securely store your Google Gemini API key. The `.env` file should be placed in the same directory as your code.

**Example `.env` file:**
```env
GEMINI_API_KEY=your-gemini-api-key-here
```

- Never share your `.env` file or commit it to version control (e.g., GitHub).
- Get your Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey).

### Loading Environment Variables in Python

This project uses the [`python-dotenv`](https://pypi.org/project/python-dotenv/) package to load environment variables from the `.env` file automatically. In `app.py`, the following code loads your variables:

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

1. Open your web browser and navigate to the Streamlit app (usually `http://localhost:8501`)
2. Enter any topic in the text input field (e.g., "Space", "Animals", "History")
3. Click "Generate Fun Fact" to get an AI-generated fun fact about your chosen topic
4. The fact will appear in a green success box below the input

## 🛠️ Prerequisites

- Python 3.8 or higher
- A Google account and Gemini API key ([get yours here](https://makersuite.google.com/app/apikey))
- Internet connection

## 📁 File Structure

- `app.py` — Main Streamlit application script
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation (this file)

## 🧑‍💻 Code Explainer

This project is a simple yet powerful web application that leverages Google's Gemini AI to generate interesting facts. Here's how it works:

1. **Environment Setup**: Loads your Gemini API key from a `.env` file using `python-dotenv`.
2. **Gemini Configuration**: Initializes the Google Generative AI client with your API key.
3. **Fun Fact Generation**: 
   - Uses the `generate_fun_fact()` function to create a prompt for the AI
   - Sends the prompt to Gemini's `gemini-1.5-flash` model
   - Returns the AI-generated response
4. **Streamlit Interface**: 
   - Provides a clean, user-friendly web interface
   - Includes input validation to ensure a topic is entered
   - Displays results in an attractive format with success/warning messages

✨ The application is designed to be educational and entertaining, perfect for students and curious minds! 🎉

## ✨ Further Enhancements

Want to take this project further? Here are some ideas:

- 🎯 **Multiple Facts**: Modify the code to generate multiple facts at once
- 📚 **Fact Categories**: Add predefined categories (Science, History, Geography, etc.)
- 💾 **Save Favorites**: Add functionality to save interesting facts to a local file
- 🎨 **Custom Styling**: Enhance the UI with custom CSS and animations
- 🔄 **Fact History**: Keep track of previously generated facts
- 🌍 **Multi-language Support**: Add support for generating facts in different languages
- 📱 **Mobile Optimization**: Improve the mobile experience with responsive design

Feel free to experiment and make it your own! 🚀 