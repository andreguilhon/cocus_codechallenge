from rest_framework import serializers
from .models import FileContent


class FileContentSerializer(serializers.Serializer):
    line_number = serializers.IntegerField()
    line_content = serializers.CharField()
    frequent_char = serializers.CharField()