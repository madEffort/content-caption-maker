from django.urls import path
from . import views

app_name = "caption"

urlpatterns = [
    path('make-caption/', views.MakeCaptionAPIView.as_view(), name='make-caption'),
]