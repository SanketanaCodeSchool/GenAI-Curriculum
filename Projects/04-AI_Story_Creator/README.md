# AI Storybook Creator

## Table of Contents
- [🛠️ Prerequisites](#prerequisites)
- [⚙️ Setup](#setup)
- [🔑 .env & Environment Variables](#env--environment-variables)
- [💬 Usage](#usage)
- [📁 File Structure](#file-structure)
- [🧑‍💻 Code Explainer](#code-explainer)
- [✨ Further Enhancements](#further-enhancements)

An innovative AI-powered application that creates personalized stories with AI-generated illustrations, perfect for students and creative writers.

## Setup

1. Install dependencies:
```bash
pip install streamlit openai python-dotenv pillow huggingface-hub requests httpx
```

2. Create `.env` file:
```bash
# Create .env file and add your API keys
OPENAI_API_KEY=your-openai-api-key-here
HUGGINGFACE_TOKEN=your-huggingface-token-here
```

3. Run the application:
```bash
streamlit run app.py
```

## .env & Environment Variables

This project uses a `.env` file to securely store your API keys for both OpenAI and Hugging Face. The `.env` file should be placed in the same directory as your code.

**Example `.env` file:**
```env
OPENAI_API_KEY=your-openai-api-key-here
HUGGINGFACE_TOKEN=your-huggingface-token-here
```

- Never share your `.env` file or commit it to version control (e.g., GitHub).
- Get your OpenAI API key from [OpenAI Platform](https://platform.openai.com/account/api-keys).
- Get your Hugging Face token from [Hugging Face](https://huggingface.co/settings/tokens).

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
hf_token = os.getenv('HUGGINGFACE_TOKEN')
```

## Usage

1. Open your web browser and navigate to the Streamlit app (usually `http://localhost:8501`)
2. Enter a story prompt in the left column (e.g., "A magical garden where plants can talk")
3. Select the appropriate age group from the dropdown in the right column:
   - Elementary (6-10)
   - Middle School (11-13)
   - High School (14-18)
4. Click "Generate Story" to create your personalized story
5. The application will:
   - Generate a story using OpenAI's GPT-3.5-turbo
   - Create a custom illustration using Hugging Face's Stable Diffusion
   - Display the story with the illustration
   - Provide a download link for the complete story as an HTML file

## 🛠️ Prerequisites

- Python 3.8 or higher
- An OpenAI account and API key ([get yours here](https://platform.openai.com/account/api-keys))
- A Hugging Face account and token ([get yours here](https://huggingface.co/settings/tokens))
- Internet connection

## 📁 File Structure

- `app.py` — Main Streamlit application script
- `requirements.txt` — Python dependencies
- `README.md` — Project documentation (this file)

## 🧑‍💻 Code Explainer

This project is a sophisticated AI-powered story creation tool that combines text generation with image creation. Here's how it works:

### Core Components:

1. **Story Generation**:
   - Uses OpenAI's `gpt-3.5-turbo` model for story creation
   - `generate_story()` function creates age-appropriate, educational content
   - Includes moral lessons and engaging narratives
   - Approximately 300 words per story

2. **Image Generation**:
   - Uses Hugging Face's Stable Diffusion XL model
   - `generate_image()` function creates child-friendly illustrations
   - Enhanced prompts ensure safe, colorful, and engaging artwork
   - Retry mechanism handles API loading delays

3. **User Interface**:
   - Clean, two-column layout using Streamlit
   - Custom CSS styling for better presentation
   - Responsive design with proper spacing and typography
   - Real-time feedback with loading spinners

4. **Content Management**:
   - Automatic story paragraph splitting for better formatting
   - Image generation based on story content
   - HTML export functionality for story downloads
   - Error handling for API failures

### Key Features:
- **Dual AI Integration**: Combines OpenAI for text and Hugging Face for images
- **Age-Appropriate Content**: Tailored stories for different educational levels
- **Educational Focus**: Stories include moral lessons and learning elements
- **Professional Output**: High-quality illustrations and formatted text
- **Downloadable Content**: Export stories as HTML files for sharing

### Technical Highlights:
- **Retry Logic**: Handles API loading delays gracefully
- **Error Handling**: Comprehensive error management with user feedback
- **Memory Management**: Efficient handling of image data and temporary files
- **Cross-Platform**: Works on various operating systems

✨ Perfect for students, teachers, parents, and anyone who loves creative storytelling! 📚

## ✨ Further Enhancements

Want to take this project further? Here are some ideas:

- 🎨 **Multiple Illustration Styles**: Add different art styles (cartoon, realistic, watercolor)
- 📖 **Chapter Generation**: Create multi-chapter stories with illustrations for each chapter
- 🎭 **Character Development**: Add character creation and development features
- 🌍 **Multi-language Stories**: Support for creating stories in different languages
- 📱 **Mobile App**: Convert to a mobile application for on-the-go story creation
- 🎵 **Audio Narration**: Add text-to-speech for story narration
- 📊 **Story Analytics**: Track popular themes and user preferences
- 🤝 **Collaborative Stories**: Allow multiple users to contribute to stories
- 🎯 **Educational Themes**: Add specific educational topics and subjects
- 💾 **Story Library**: Save and organize created stories
- 🎨 **Custom Illustrations**: Allow users to upload their own images
- 📚 **Story Templates**: Provide templates for different story types (adventure, mystery, fantasy)

Feel free to experiment and make it your own! 🚀 