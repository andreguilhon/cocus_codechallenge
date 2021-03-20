from rest_framework import views
from rest_framework.response import Response
from .controllers import FileReaderController

class FileContentViews(views.APIView):
    def get(self, request, line_number=None):
        return Response(FileReaderController().read_line(line_number))
