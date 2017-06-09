
from bs4 import BeautifulSoup
import requests

def get_Nobel_soup():
    response = requests.get('https://en.wikipedia.org/wiki/List_of_Nobel_laureates')
    returns BeautifulSoup4(response.content, "lxml")

soup = get_Nobel_soup
print(soup)
