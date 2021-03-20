from os import path, read
from linecache import getline
from random import randint


class FileReaderController:
    def read_line(self, line_number=None):
        filename = path.join(path.dirname(__file__), 'quotes.txt')
        print(filename)
        if not line_number:
            line_number = randint(0,50)
        
        return {'line_content': getline(filename, line_number).rstrip(), 'line_number': line_number}