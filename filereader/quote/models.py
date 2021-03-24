from django.db import models
from django.db.models.aggregates import Count
from random import randint


class Quote(models.Model):
    line_content = models.TextField()
    line_number = models.IntegerField(unique=True)
    most_common_character = models.CharField(max_length=1)

    def __str__(self) -> str:
        return f'[{self.line_number}] - {self.line_content}'