from django.urls import path
from . import views

app_name = "caption"

urlpatterns = [
    path('', views.home, name='home'),
    # path('transcribe_video/', views.transcribe_video, name='transcribe_video'),
    # path('transcription_progress/', views.transcription_progress, name='transcription_progress'),
    path('make-caption/', views.make_caption, name='make-caption'),
]