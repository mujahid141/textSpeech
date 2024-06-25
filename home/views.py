# tts_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
from gtts import gTTS
from .models import Speech

def text_to_speech(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        speech = gTTS(text , lang='en' ) 
        audio_file_path = f'home/static/audio.mp3'
        speech.save(audio_file_path)

        # If you are saving the audio to the database
        # Speech.objects.create(text=text, audio_file=audio_file_path)

        return render(request, 'audio.html')
    return render(request, 'index.html')  # Create an HTML template for user input
def play_audio(request):
    return render(request, 'audio.html')