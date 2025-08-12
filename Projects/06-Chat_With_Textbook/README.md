# Chat With Your Textbook

## Table of Contents
- [🛠️ Prerequisites](#prerequisites)
- [⚙️ Setup](#setup)
- [🔑 .env & Environment Variables](#env--environment-variables)
- [💬 Usage](#usage)
- [📁 File Structure](#file-structure)
- [🧑‍💻 Code Explainer](#code-explainer)
- [✨ Further Enhancements](#further-enhancements)

An intelligent AI-powered application that allows you to upload textbooks and chat with them using OpenAI's GPT-4. Features both basic and advanced versions with OCR capabilities for scanned documents.

## Setup

1. Install dependencies:
```bash
pip install streamlit PyPDF2 pdf2image Pillow openai python-dotenv tiktoken
```

2. Create `.env` file:
```bash
# Copy the template file and rename it to .env
cp env_template.txt .env
# Edit .env and add your actual OpenAI API key
```

3. Run the application:
```bash
# For basic version (text-based PDFs only)
streamlit run app_basic.py

# For advanced version (supports scanned PDFs with OCR)
streamlit run app_advanced.py
```

## .env & Environment Variables

This project uses a `.env` file to securely store your OpenAI API key. The `.env` file should be placed in the same directory as your code.

**Example `.env` file:**
```env
OPENAI_API_KEY=your-actual-openai-api-key-here
```

- Never share your `.env` file or commit it to version control (e.g., GitHub).
- Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/account/api-keys).

### Loading Environment Variables in Python

This project uses the [`python-dotenv`](https://pypi.org/project/python-dotenv/) package to load environment variables from the `.env` file automatically. In both `app_basic.py` and `app_advanced.py`, the following code loads your variables:

```python
from dotenv import load_dotenv
load_dotenv()
```

You can then access your API key using:

```python
import os
api_key = os.getenv('OPENAI_API_KEY')
```

## Usage

### Basic Version (`app_basic.py`)
1. Open your web browser and navigate to the Streamlit app
2. Upload a PDF with digital text (not scanned images)
3. Enter a name for your book and save it
4. Select your book from the dropdown menu
5. Start chatting with your textbook by asking questions
6. The AI will answer based on the content of your uploaded book

### Advanced Version (`app_advanced.py`)
1. Open your web browser and navigate to the Streamlit app
2. Upload any PDF (digital text or scanned images)
3. The app will automatically extract text using:
   - Direct text extraction for digital PDFs
   - GPT-4 Vision OCR for scanned PDFs
4. Enter a unique name for your book and save it
5. Select your book and start chatting
6. View token usage and manage your conversations

## 🛠️ Prerequisites

- Python 3.8 or higher
- An OpenAI account and API key ([get yours here](https://platform.openai.com/account/api-keys))
- Internet connection
- For advanced version: Poppler installed on your system for PDF processing

### Installing Poppler (for advanced version)

**macOS:**
```bash
brew install poppler
```

**Ubuntu/Debian:**
```bash
sudo apt-get install poppler-utils
```

**Windows:**
Download from [Poppler for Windows](https://github.com/oschwartz10612/poppler-windows/releases/)

## 📁 File Structure

- `app_basic.py` — Basic version for digital text PDFs only
- `app_advanced.py` — Advanced version with OCR support for scanned PDFs
- `requirements.txt` — Python dependencies
- `env_template.txt` — Template for environment variables (copy to `.env` and add your API keys)
- `scanned_books/` — Directory where uploaded books are stored
- `sample_input/` — Sample PDF files for testing
- `README.md` — Project documentation (this file)

## 🧑‍💻 Code Explainer

This project features two versions of an AI-powered textbook chat application:

### Basic Version (`app_basic.py`)
- **PDF Text Extraction**: Uses PyPDF2 to extract text from digital PDFs
- **Book Management**: Allows users to upload, name, and save books
- **Chat Interface**: Simple chat interface with conversation history
- **Context Awareness**: Each book maintains its own conversation context
- **Error Handling**: Graceful error handling for file uploads and processing

### Advanced Version (`app_advanced.py`)
- **Dual Extraction Methods**: 
  - Direct text extraction for digital PDFs
  - GPT-4 Vision OCR for scanned PDFs using pdf2image
- **Token Management**: Tracks token usage with tiktoken
- **Enhanced UI**: Better progress tracking and user feedback
- **File Validation**: Prevents duplicate book names and validates uploads
- **Image Processing**: Converts PDF pages to images for OCR processing

### Key Components:
1. **Environment Setup**: Loads OpenAI API key from `.env` file
2. **PDF Processing**: Handles both digital and scanned PDFs
3. **Text Extraction**: Multiple methods for extracting text content
4. **OpenAI Integration**: Uses GPT-4 for intelligent responses
5. **Session Management**: Maintains conversation history per book
6. **File Storage**: Organizes uploaded books in local directory

✨ Perfect for students, researchers, and anyone who wants to interact with their textbooks using AI! 📚

## ✨ Further Enhancements

Want to take this project further? Here are some ideas:

- 📊 **Multiple Books**: Allow chatting with multiple books simultaneously
- 🔍 **Search Functionality**: Add search capabilities within book content
- 📝 **Note Taking**: Allow users to save important parts of conversations
- 🎯 **Quiz Generation**: Generate quizzes based on book content
- 📚 **Citation Support**: Add page numbers and citations to responses
- 🌍 **Multi-language**: Add support for books in different languages
- 📱 **Mobile Optimization**: Improve the mobile experience
- 💾 **Cloud Storage**: Add cloud storage for books and conversations
- 🎨 **Custom Styling**: Enhance the UI with custom CSS and themes
- 🔄 **Export Conversations**: Allow users to export chat history
- 📖 **Book Recommendations**: Suggest related books based on content
- 🎓 **Study Groups**: Add collaborative features for group study

Feel free to experiment and make it your own! 🚀 