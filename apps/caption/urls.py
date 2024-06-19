from django.urls import path
from . import views

app_name = "caption"

urlpatterns = [
    path('', views.home, name='home'),
    path('transcribe_video/', views.transcribe_video, name='transcribe_video'),
]