import requests
from bs4 import BeautifulSoup

base_url = 'http://books.toscrape.com/'
url = 'http://books.toscrape.com/catalogue/sharp-objects_997/index.html'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')



