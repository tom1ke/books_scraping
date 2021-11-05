import requests
from bs4 import BeautifulSoup
from word2number import w2n
import csv
import time
import re
from urllib.parse import urljoin

# ---SETUP---
start_time = time.time()

base_url = 'http://books.toscrape.com'
url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

book_list = []

# ---FUNCTIONS---


def get_books_url():
    books = soup.find_all('h3')
    for book in books:
        books_href = book.find('a')['href']
        books_url = urljoin(base_url, books_href)
        book_list.append(books_url)


def write_info_csv():
    with open(f'data/script_2/{category}.csv', 'a+', encoding='utf-8-sig') as csv_file:
        file_empty = os.stat(f'data/script_2/{category}.csv').st_size == 0
        writer = csv.DictWriter(csv_file, output)
        if file_empty:
            writer.writeheader()
        writer.writerow(output)


def get_image():
    download_image = requests.get(image_url).content
    with open(f'data/script_2/images/{title}.jpg', 'wb') as jpg_file:
        jpg_file.write(download_image)


get_books_url()

print(book_list)

print(time.time() - start_time, "seconds")
