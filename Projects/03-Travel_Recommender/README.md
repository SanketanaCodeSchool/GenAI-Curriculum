# AI Travel Destination Recommender

## Table of Contents
- [🛠️ Prerequisites](#prerequisites)
- [⚙️ Setup](#setup)
- [🔑 .env & Environment Variables](#env--environment-variables)
- [💬 Usage](#usage)
- [📁 File Structure](#file-structure)
- [🧑‍💻 Code Explainer](#code-explainer)
- [✨ Further Enhancements](#further-enhancements)

An intelligent travel recommendation system that uses AI to suggest personalized travel destinations based on your preferences for climate, activities, budget, and trip duration.

## Setup

1. Install dependencies:
```bash
pip install streamlit google-generativeai python-dotenv pillow
```

2. Create `.env` file:
```bash
# Copy the template file and rename it to .env
cp env_template.txt .env
# Edit .env and add your actual Gemini API key
```

3. Run the application:
```bash
streamlit run app.py
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
2. Fill in your travel preferences:
   - **Climate**: Choose from Tropical, Mediterranean, Cold/Snow, Desert, or Temperate
   - **Activities**: Select from Beach & Relaxation, Adventure & Sports, Cultural & Historical, Nature & Wildlife, or Food & Shopping
   - **Budget**: Choose Budget/Backpacker, Mid-range, or Luxury
   - **Duration**: Use the slider to select your trip duration (3-30 days)
3. Click "Get Recommendations! 🎯" to receive personalized travel suggestions
4. The AI will provide 3 detailed destination recommendations with:
   - City and Country
   - Main attractions
   - Estimated daily budget
   - Best time to visit
   - One unique fact about each destination

## 🛠️ Prerequisites

- Python 3.8 or higher
- A Google account and Gemini API key ([get yours here](https://makersuite.google.com/app/apikey))
- Internet connection

## 📁 File Structure

- `app.py` — Main Streamlit application script
- `requirements.txt` — Python dependencies
- `env_template.txt` — Template for environment variables (copy to `.env` and add your API keys)
- `README.md` — Project documentation (this file)

## 🧑‍💻 Code Explainer

This project is an intelligent travel recommendation system that leverages Google's Gemini AI to provide personalized travel suggestions. Here's how it works:

### Core Components:

1. **User Interface**: 
   - Clean, intuitive Streamlit interface with dropdown menus and sliders
   - Organized input sections for different preference categories
   - Visual feedback with balloons animation on successful recommendations

2. **AI Integration**:
   - Uses Google's `gemini-1.5-flash` model for intelligent recommendations
   - Structured prompts ensure consistent, detailed responses
   - Error handling for API failures with user-friendly messages

3. **Recommendation Engine**:
   - `get_travel_recommendations()` function crafts detailed prompts
   - Considers climate, activity type, budget, and duration preferences
   - Returns comprehensive destination information including attractions, costs, and timing

4. **User Experience**:
   - Real-time feedback with loading spinners
   - Clear, formatted output with structured information
   - Celebration animation (balloons) for successful recommendations

### Key Features:
- **Personalized Suggestions**: AI considers multiple factors for tailored recommendations
- **Comprehensive Information**: Each recommendation includes attractions, budget, timing, and unique facts
- **User-Friendly Interface**: Intuitive controls and clear visual feedback
- **Error Handling**: Graceful handling of API issues and user input validation

✨ Perfect for students planning trips, travelers seeking inspiration, or anyone looking for AI-powered travel guidance! 🌎

## ✨ Further Enhancements

Want to take this project further? Here are some ideas:

- 🗺️ **Interactive Maps**: Integrate with mapping APIs to show destination locations
- 📸 **Image Gallery**: Add photos of recommended destinations
- 💰 **Budget Calculator**: Create detailed budget breakdowns for each destination
- 📅 **Seasonal Recommendations**: Factor in current season and weather patterns
- 🏨 **Accommodation Suggestions**: Include hotel and lodging recommendations
- 🍽️ **Local Cuisine**: Add information about local food and restaurants
- 🚗 **Transportation Tips**: Include getting around information for each destination
- 📱 **Mobile Optimization**: Improve mobile experience with responsive design
- 🌍 **Multi-language Support**: Add support for different languages
- 💾 **Save Favorites**: Allow users to save and compare different recommendations
- 📊 **Travel Statistics**: Show popularity and rating data for destinations
- 🎯 **Specialized Themes**: Add themed recommendations (honeymoon, family, solo travel)

Feel free to experiment and make it your own! 🚀 