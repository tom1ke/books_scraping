import requests
from bs4 import BeautifulSoup
from word2number import w2n
import csv
import time
import re

start_time = time.time()

base_url = 'http://books.toscrape.com/'
url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


def get_books_url():
    books = soup.find_all('div', class_='image_container')
    for book in books:
        return book.find('a')['href']


with open(f'data/{category}.csv', 'a+', encoding='utf-8-sig') as csv_file:
    file_empty = os.stat(f'data/{title}.csv').st_size == 0
    writer = csv.DictWriter(csv_file, output)
    if file_empty:
        writer.writeheader()
    writer.writerow(output)

print(time.time() - start_time, "seconds")
