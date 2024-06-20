from django.urls import path
from . import views

app_name = "caption"

urlpatterns = [
    path('', views.home, name='home'),
    path('make-caption/', views.make_caption, name='make-caption'),
]