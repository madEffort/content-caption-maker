import os
import subprocess
import logging

from django.core.files.storage import FileSystemStorage
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


# 로거 설정
logger = logging.getLogger(__name__)


class MakeCaptionAPIView(APIView):

    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):

        if "file" not in request.FILES:
            return Response(
                {"error": "Please upload a video file."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        try:
            video_file = request.FILES["file"]
            fs = FileSystemStorage()
            filename = fs.save(video_file.name, video_file)
            file_path = fs.path(filename)

            # Whisper 명령어 실행
            command = ["faster-whisper", file_path, "--model", "base"]
            subprocess.run(command, capture_output=True, text=True)

            srt_filename = filename.rsplit(".", 1)[0] + ".srt"
            srt_path = os.path.join(fs.location, srt_filename)

            if os.path.exists(srt_path):
                fs.delete(filename)
                return Response({"success": True}, status=status.HTTP_200_OK)
            else:
                fs.delete(filename)
                return Response(
                    {"error": "SRT file not found."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
        except Exception as e:
            logger.error(f"Error during processing: {e}")
            fs.delete(filename)

        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
