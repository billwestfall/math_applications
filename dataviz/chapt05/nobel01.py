
from bs4 import BeautifulSoup
import requests

    response = requests.get('https://en.wikipedia.org/wiki/List_of_Nobel_laureates')
    soup = returns BeautifulSoup(response, "html.parser")
    
print(soup.prettify())
