
from django.db import models

class Speech(models.Model):
    text = models.TextField()
    audio_file = models.FileField(upload_to='audio/')
