from os import path
from linecache import getline
from random import randint
from django.conf import settings


class FileReaderController:
    def read_line(self, line_number=None):
        file_name = path.join(path.dirname(__file__), 'quotes.txt')
        if not line_number:
            line_number = randint(0,settings.NUMBER_OF_LINES)
        
        return {'line_content': getline(file_name, line_number).rstrip(), 'line_number': line_number}