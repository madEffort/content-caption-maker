from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from .models import Video
import whisper
import os


# Create your views here.
def home(request):
    return render(request, 'home.html')

def transcribe_video(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        video = Video.objects.create(file=file)
        
        file_path = os.path.join(settings.MEDIA_ROOT, video.file.name)
        
        model = whisper.load_model("base")
        
        try:
            result = model.transcribe(file_path)
            return JsonResponse({'video_url': video.file.url, 'transcribed_text': result['text']}, status=200)
        except RuntimeError as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)