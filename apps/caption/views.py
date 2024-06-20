from django.shortcuts import render
from django.http import JsonResponse
from .models import Video
import os
import subprocess
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    return render(request, 'home.html')

def make_caption(request):
    if request.method == 'POST' and request.FILES.get('file'):
        video_file = request.FILES['file']
        fs = FileSystemStorage()
        filename = fs.save(video_file.name, video_file)
        file_path = fs.path(filename)

        # Whisper 명령어 실행
        command = ["faster-whisper", file_path, "--model", "base"]
        subprocess.run(command, capture_output=True, text=True)

        # Assuming that the Whisper command generates an .srt file in the same directory
        srt_filename = filename.rsplit('.', 1)[0] + '.srt'
        srt_path = os.path.join(fs.location, srt_filename)

        # Read the .srt file contents
        # if os.path.exists(srt_path):
        #     with open(srt_path, 'r', encoding='utf-8') as srt_file:
        #         srt_content = srt_file.read()

        #     # Clean up
        #     fs.delete(filename)
            # os.remove(srt_path)
        
        if os.path.exists(srt_path):
            fs.delete(filename)
            return JsonResponse({'success': True}, status=200)
        else:
            fs.delete(filename)
            return JsonResponse({'error': "SRT file not found."}, status=500)

    return JsonResponse({'error': "Please upload a video file."}, status=400)
