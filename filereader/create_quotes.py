import requests

quotes = requests.get('https://goquotes-api.herokuapp.com/api/v1/all/quotes')
# quotes = requests.get('https://goquotes-api.herokuapp.com/api/v1/random?count=1')

quotes = quotes.json().get('quotes')
with open('filereader/reader/quotes.txt', 'a') as f:
    for quote in quotes[:-1]:
        f.write(f"{quote.get('text')} - {quote.get('author')}\n")