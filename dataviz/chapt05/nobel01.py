
from bs4 import BeautifulSoup

html_doc = "https://en.wikipedia.org/wiki/List_of_Nobel_laureates"
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
