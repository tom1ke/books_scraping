import requests
from bs4 import BeautifulSoup
from word2number import w2n
import csv
import time
import re
import os
from urllib.parse import urljoin

start_time = time.time()

# ---SETUP---

base_url = 'http://books.toscrape.com'
# url = 'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html'
#
# page = requests.get(url)
# soup = BeautifulSoup(page.content, 'html.parser')

book_list = []

# ---FUNCTIONS---


def read_page(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, 'html.parser') as soup


def get_books_url():
    read_page('http://books.toscrape.com/catalogue/category/books/mystery_3/index.html')
    books = soup.find_all('h3')
    find_next = soup.find_all('li', class_='next')[0].find('a')['href']
    next_url = urljoin(url, find_next)
    print(next_url)
    for book in books:
        books_href = book.find('a')['href']
        books_url = urljoin(url, books_href)
        book_list.append(books_url)
        if not find_next:
            break
        read_page(next_url)

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


# --- MAIN ---


get_books_url()
print(book_list)

# for _ in book_list:
#     # ---SCRAPING---
#     title = soup.find('h1').text
#
#     category = soup.find_all('a')[3].text
#
#     review_rating = soup.find_all('p', class_='star-rating')[0].get('class')[1]
#     review_rating = w2n.word_to_num(review_rating)
#
#     product_description = soup.find_all('article')[0].find_all('p')[3].text
#
#     upc = soup.find_all('td')[0].text
#
#     price_tax_excl = soup.find_all('td')[2].text
#
#     price_tax_incl = soup.find_all('td')[3].text
#
#     number_available = soup.find_all('td')[5].text
#     number_available = re.sub("[^0-9]", "", number_available)
#
#     image_url = soup.find('img')['src']
#     image_url = urljoin(base_url, image_url)
#
#     # ---BOOK INFO TO DICTIONARY---
#     output = {variable: eval(variable) for variable in ['title',
#                                                         'category',
#                                                         'review_rating',
#                                                         'product_description',
#                                                         'upc',
#                                                         'price_tax_excl',
#                                                         'price_tax_incl',
#                                                         'number_available',
#                                                         'image_url',
#                                                         'url']}

    # ---WRITING CSV & GETTIN IMAGE---
    # write_info_csv()
    #
    # get_image()


print(time.time() - start_time, "seconds")
