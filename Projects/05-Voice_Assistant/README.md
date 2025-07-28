# AI Voice Assistant

## Table of Contents
- [🛠️ Prerequisites](#prerequisites)
- [⚙️ Setup](#setup)
- [🔑 .env & Environment Variables](#env--environment-variables)
- [💬 Usage](#usage)
- [📁 File Structure](#file-structure)
- [🧑‍💻 Code Explainer](#code-explainer)
- [✨ Further Enhancements](#further-enhancements)

An advanced AI voice assistant that combines speech-to-text, AI chat, and text-to-speech capabilities using OpenAI and ElevenLabs APIs.

## Setup

1. Install dependencies:
```bash
pip install gradio openai python-dotenv elevenlabs
```

2. Create `.env` file:
```bash
# Create .env file and add your API keys
OPENAI_API_KEY=your-openai-api-key-here
ELEVENLABS_API_KEY=your-elevenlabs-api-key-here
```

3. Run the application:
```bash
python app.py
```

## .env & Environment Variables

This project uses a `.env` file to securely store your API keys for both OpenAI and ElevenLabs. The `.env` file should be placed in the same directory as your code.

**Example `.env` file:**
```env
OPENAI_API_KEY=your-openai-api-key-here
ELEVENLABS_API_KEY=your-elevenlabs-api-key-here
```

- Never share your `.env` file or commit it to version control (e.g., GitHub).
- Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/account/api-keys).
- Get your ElevenLabs API key from [ElevenLabs](https://elevenlabs.io/).

### Loading Environment Variables in Python

This project uses the [`python-dotenv`](https://pypi.org/project/python-dotenv/) package to load environment variables from the `.env` file automatically. In `app.py`, the following code loads your variables:

```python
from dotenv import load_dotenv
load_dotenv()
```

You can then access your API keys using:

```python
import os
openai_key = os.getenv('OPENAI_API_KEY')
elevenlabs_key = os.getenv('ELEVENLABS_API_KEY')
```

## Usage

1. Open your web browser and navigate to the Gradio app (usually `http://localhost:7860`)
2. **Record or Upload Audio**:
   - Use the microphone to record your voice directly in the browser
   - Or upload an audio file from your device
3. **Select Voice**: Choose from the dropdown menu of available ElevenLabs voices
4. **Submit**: Click the "Submit" button to process your audio
5. **View Results**: The application will display:
   - **Transcription**: Your speech converted to text
   - **AI Response**: ChatGPT's response to your message
   - **Audio Response**: AI-generated speech response using your selected voice

## 🛠️ Prerequisites

- Python 3.8 or higher
- An OpenAI account and API key ([get yours here](https://platform.openai.com/account/api-keys))
- An ElevenLabs account and API key ([get yours here](https://elevenlabs.io/))
- Internet connection
- Microphone (for voice recording)

## 📁 File Structure

- `app.py` — Main Gradio application script
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation (this file)

## 🧑‍💻 Code Explainer

This project is a sophisticated voice assistant that combines multiple AI technologies for a complete voice interaction experience. Here's how it works:

### Core Components:

1. **Speech-to-Text (STT)**:
   - Uses OpenAI's `gpt-4o-transcribe` model
   - `speech_to_text()` function converts audio to text
   - Supports various audio formats and quality levels
   - Handles different accents and speech patterns

2. **AI Chat Processing**:
   - Uses OpenAI's `gpt-4.1` model for intelligent responses
   - `get_chat_completion()` function processes user input
   - Maintains context and provides relevant responses
   - Handles complex queries and conversations

3. **Text-to-Speech (TTS)**:
   - Uses ElevenLabs' advanced TTS technology
   - `text_to_speech()` function converts AI responses to speech
   - Multiple voice options available
   - High-quality, natural-sounding audio output

4. **Voice Management**:
   - `get_available_voices()` fetches all available ElevenLabs voices
   - Dynamic voice selection dropdown
   - Fallback voice handling for reliability
   - Voice customization options

5. **User Interface**:
   - Clean Gradio interface with intuitive layout
   - Real-time audio recording and playback
   - Clear input/output sections
   - Error handling and user feedback

### Key Features:
- **Complete Voice Pipeline**: From speech input to AI response to speech output
- **Multiple Voice Options**: Choose from various ElevenLabs voices
- **High-Quality Audio**: Professional-grade speech synthesis
- **Flexible Input**: Record directly or upload audio files
- **Real-Time Processing**: Quick response times for natural conversation

### Technical Highlights:
- **Error Handling**: Comprehensive error management for all API calls
- **Temporary File Management**: Efficient handling of audio files
- **API Integration**: Seamless integration of multiple AI services
- **Cross-Platform**: Works on various operating systems and browsers

✨ Perfect for accessibility applications, language learning, or anyone who prefers voice interaction! 🎙️

## ✨ Further Enhancements

Want to take this project further? Here are some ideas:

- 🎯 **Voice Commands**: Add specific voice command recognition for different actions
- 📱 **Mobile App**: Convert to a mobile application for on-the-go use
- 🌍 **Multi-language Support**: Add support for multiple languages
- 🎵 **Voice Cloning**: Allow users to clone their own voice
- 📊 **Conversation History**: Save and manage conversation logs
- 🎨 **Custom Voices**: Create and train custom voice models
- 🔄 **Continuous Listening**: Add always-on listening mode
- 📝 **Voice Notes**: Convert voice to text notes for productivity
- 🎭 **Voice Acting**: Add different voice personalities and styles
- 🔒 **Privacy Features**: Add local processing options for sensitive conversations
- 📈 **Usage Analytics**: Track usage patterns and preferences
- 🤝 **Multi-user Support**: Allow multiple users with different voice preferences

Feel free to experiment and make it your own! 🚀 