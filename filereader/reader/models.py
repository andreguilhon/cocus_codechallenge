# from django.db import models

# Create your models here.
class FileContent:
    line_number = 0
    line_content = ''
    frequent_char = ''
    
    def __init__(self, line_number, line_content, frequent_Char) -> None:
        self.line_number = line_number
        self.line_content = line_content
        self.frequent_char = frequent_Char

    