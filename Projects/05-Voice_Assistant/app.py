import gradio as gr
from openai import OpenAI
from dotenv import load_dotenv
import os
from pathlib import Path
import tempfile
from elevenlabs import ElevenLabs, voices, save

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

# Initialize ElevenLabs client
elevenlabs_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

def speech_to_text(audio_file):
    """
    Convert speech to text using OpenAI's transcription API
    """
    try:
        with open(audio_file, "rb") as f:
            transcription = client.audio.transcriptions.create(
                model="gpt-4o-transcribe",
                file=f,
                response_format="text"
            )
        return transcription
    except Exception as e:
        print(f"Error in speech_to_text: {e}")
        raise

def get_chat_completion(user_message):
    """
    Get response from ChatGPT based on user input
    """
    try:
        completion = client.chat.completions.create(
            model="gpt-4.1",
            messages=[{"role": "user", "content": user_message}]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error in get_chat_completion: {e}")
        raise

def text_to_speech(text, voice="21m00Tcm4TlvDq8ikWAM"):
    """
    Convert text to speech using ElevenLabs TTS API
    """
    try:
        speech_file_path = Path(tempfile.gettempdir()) / "response.mp3"
        
        # Generate audio using ElevenLabs (returns a generator/stream)
        audio_stream = elevenlabs_client.text_to_speech.convert(
            text=text,
            voice_id=voice,
            model_id="eleven_monolingual_v1"
        )
        
        # Save the audio file from the generator/stream
        with open(speech_file_path, "wb") as f:
            for chunk in audio_stream:
                f.write(chunk)
        
        return str(speech_file_path)
    except Exception as e:
        print(f"Error in text_to_speech: {e}")
        raise

def get_available_voices():
    """
    Get list of available ElevenLabs voices
    """
    try:
        available_voices = elevenlabs_client.voices.get_all()
        # Create a list of (name, id) tuples for the dropdown
        voice_options = [(f"{voice.name} ({voice.voice_id})", voice.voice_id) for voice in available_voices.voices]
        return voice_options
    except Exception as e:
        print(f"Error getting voices: {e}")
        # Return a fallback voice if there's an error
        return [("Default (EXAVITQu4vr4xnSDxMaL)", "EXAVITQu4vr4xnSDxMaL")]

def get_default_voice():
    """
    Get the first available voice as default
    """
    try:
        voices = get_available_voices()
        if voices:
            return voices[0][1]  # Return the first voice ID
        return "EXAVITQu4vr4xnSDxMaL"  # Fallback
    except:
        return "EXAVITQu4vr4xnSDxMaL"  # Fallback

def process_audio(audio_file, selected_voice):
    """
    Main function that orchestrates the voice assistant workflow
    """
    try:
        print("audio_file:", audio_file)
        print("selected_voice:", selected_voice)
        
        # Step 1: Convert speech to text
        transcription = speech_to_text(audio_file)
        
        # Step 2: Get AI response
        response = get_chat_completion(transcription)
        
        # Step 3: Convert response to speech using selected voice
        speech_file_path = text_to_speech(response, selected_voice)
        
        return transcription, response, speech_file_path
    except Exception as e:
        print("Error in process_audio:", e)
        return "Error", "Error", "Error"

# Create Gradio interface
with gr.Blocks(title="AI Voice Assistant") as demo:
    gr.Markdown("# 🎙️ AI Voice Assistant")
    gr.Markdown("Record your voice or upload an audio file to chat with the AI assistant.")
    
    with gr.Row():
        with gr.Column():
            audio_input = gr.Audio(
                type="filepath",
                label="Record your voice"
            )
            voice_dropdown = gr.Dropdown(
                choices=get_available_voices(),
                value=get_default_voice(),
                label="Select Voice",
                info="Choose the voice for AI responses"
            )
            submit_btn = gr.Button("Submit")
        
        with gr.Column():
            transcription_output = gr.Textbox(label="Transcription")
            response_output = gr.Textbox(label="AI Response")
            audio_output = gr.Audio(label="AI Voice Response", type="filepath")
    
    submit_btn.click(
        fn=process_audio,
        inputs=[audio_input, voice_dropdown],
        outputs=[transcription_output, response_output, audio_output]
    )

if __name__ == "__main__":
    demo.launch() 