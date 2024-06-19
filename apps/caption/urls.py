from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('transcribe_video/', views.transcribe_video, name='transcribe_video'),
]