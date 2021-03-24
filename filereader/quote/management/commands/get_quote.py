from os import stat
from django.core.management.base import BaseCommand
from django.conf import settings
from quote.models import Quote
import requests
import collections



class Command(BaseCommand):
    help = 'Gets a quote from the Quote API and inserts it to Database'

    def add_arguments(self, parser):
        parser.add_argument('--number_of_quotes', type=int)

    def handle(self, *args, **options):
        number_of_quotes = options['number_of_quotes']
        if not number_of_quotes:
            number_of_quotes = 1
        for i in range(0,number_of_quotes):
            random_quote = self.__get_quote()
            line = random_quote.get('line_number')
            content = random_quote.get('line_content')
            most_common_character = self.__get_most_common_character(content, settings.INCLUDE_BLANKS)
            if most_common_character:
                self.__upsert_quote(line, content, most_common_character)

    def __upsert_quote(self, line, content, most_common_character):
        try:
            Quote.objects.get(line_number=line)
            self.stdout.write(f'Line {line} is already in the database!')
        except Quote.DoesNotExist:
            Quote(line_number=line, line_content=content, most_common_character=most_common_character).save()
            self.stdout.write(f'Saved line {line} to the database!')

    @staticmethod
    def __get_quote():
       return requests.get('http://localhost:8010/reader/').json()

    def __get_most_common_character(self, quote, include_blank):
        most_common = collections.Counter(quote).most_common(2)
        if quote.strip():
            if most_common[0][0] == ' ' and include_blank:
                return most_common[0][0]
            else:
                return most_common[1][0]
        return False
        