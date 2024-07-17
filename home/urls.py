# tts_project/urls.py
from django.urls import path
from home import views


urlpatterns = [
    # path('', views.index, name='index'),  # Home page for user input
    path('', views.text_to_speech, name='text_to_speech'),
    path('play-audio/', views.play_audio, name='play_audio'),
]
