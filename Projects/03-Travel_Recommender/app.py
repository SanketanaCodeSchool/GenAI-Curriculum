import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

def get_travel_recommendations(climate, activity, budget, duration):
    # Craft the prompt for the AI
    prompt = f"""
    Suggest 3 travel destinations based on these preferences:
    - Preferred climate: {climate}
    - Desired activity type: {activity}
    - Budget level: {budget}
    - Trip duration: {duration} days
    
    For each destination, provide:
    1. City and Country
    2. Main attractions
    3. Estimated daily budget
    4. Best time to visit
    5. One unique fact
    
    Format each destination separately and clearly.
    """
    
    # Get response from Gemini
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("🌎 AI Travel Destination Recommender")
    st.write("Let's help you find your perfect travel destination!")
    
    # User Input Section
    st.subheader("Your Travel Preferences")
    
    # Climate preference
    climate = st.selectbox(
        "What's your preferred climate?",
        ["Tropical", "Mediterranean", "Cold/Snow", "Desert", "Temperate"]
    )
    
    # Activity preference
    activity = st.selectbox(
        "What type of activities do you enjoy?",
        ["Beach & Relaxation", "Adventure & Sports", "Cultural & Historical",
         "Nature & Wildlife", "Food & Shopping"]
    )
    
    # Budget level
    budget = st.radio(
        "What's your budget level?",
        ["Budget/Backpacker", "Mid-range", "Luxury"]
    )
    
    # Trip duration
    duration = st.slider("How many days do you plan to travel?", 3, 30, 7)
    
    # Generate recommendations
    if st.button("Get Recommendations! 🎯"):
        with st.spinner("AI is finding perfect destinations for you..."):
            try:
                recommendations = get_travel_recommendations(
                    climate, activity, budget, duration
                )
                
                st.subheader("🌟 Your Personalized Travel Recommendations")
                st.write(recommendations)
                
                # Add a fun element for students
                st.balloons()
                
            except Exception as e:
                st.error(f"Oops! Something went wrong: {str(e)}")
                st.write("Please try again!")

if __name__ == "__main__":
    main() 