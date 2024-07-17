from django.shortcuts import render
from django.http import JsonResponse
import os
import uuid
from elevenlabs import VoiceSettings
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

# Initialize ElevenLabs client
ELEVENLABS_API_KEY = os.getenv(API_KEY)
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

# Define the text_to_speech_file function
def text_to_speech_file(text: str, language: str = 'en') -> str:
    # Determine the model_id based on the language
    if language == 'ur':
        model_id = "eleven_multilingual_v2"
    else:
        model_id = "eleven_turbo_v2"
    
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",  # Use appropriate voice for Urdu if available
        optimize_streaming_latency="0",
        output_format="mp3_22050_32",
        text=text,
        model_id=model_id,
        voice_settings=VoiceSettings(
            stability=0.0,
            similarity_boost=1.0,
            style=0.0,
            use_speaker_boost=True,
        ),
    )

    # Generating a unique file name for the output MP3 file
    filename = f"{uuid.uuid4()}.mp3"
    save_file_path = os.path.join('static/audio', filename)

    # Ensure the directory exists
    os.makedirs(os.path.dirname(save_file_path), exist_ok=True)

    # Writing the audio to a file
    with open(save_file_path, "wb") as f:
        for chunk in response:
            if chunk:
                f.write(chunk)

    print(f"{save_file_path}: A new audio file was saved successfully!")

    # Return the path of the saved audio file relative to the static directory
    return f"audio/{filename}"


# Define the text_to_speech view
def text_to_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        language = request.POST.get('language', 'ur')
        audio_file_path = text_to_speech_file(text, language)

        # If you are saving the audio to the database
        # Speech.objects.create(text=text, audio_file=audio_file_path)

        return render(request, 'audio.html', {'audio_file_path': audio_file_path})
    return render(request, 'index.html')  # Create an HTML template for user input

# Define the play_audio view
def play_audio(request):
    return render(request, 'audio.html')
