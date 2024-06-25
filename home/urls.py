# tts_project/urls.py
from django.urls import path
from home.views import text_to_speech, play_audio


urlpatterns = [
    path('text-to-speech/', text_to_speech, name='text_to_speech'),
    path('play_audio/', play_audio, name = 'play_audio' ),
    # Add other paths as needed
]
