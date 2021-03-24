from rest_framework import views
from rest_framework.response import Response
from .controllers import FileReaderController
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.renderers import JSONRenderer

class FileContentViews(views.APIView):
    renderer_classes = [JSONRenderer, XMLRenderer]
    def get(self, request, line_number=None):
        return Response(FileReaderController().read_line(line_number))
