from django.db import models

# Create your models here.
class Video(models.Model):
    file = models.FileField(upload_to='videos/')
    transcribed_text = models.TextField(blank=True, null=True)