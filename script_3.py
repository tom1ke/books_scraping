import requests
from bs4 import BeautifulSoup
from word2number import w2n
import csv
import time
import re
import os
from os.path import exists
from urllib.parse import urljoin

start_time = time.time()

# ---SETUP---

site_url = 'https://books.toscrape.com/index.html'

category_list = []
book_list = []

# ---FUNCTIONS---


def read_page(selected_url):
    global soup
    page = requests.get(selected_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def get_category_url():
    global category_url
    read_page(site_url)
    categories = soup.find_all('li')[3:53]
    print(categories)
    for category in categories:
        category_href = category.find('a')['href']
        category_url = urljoin(site_url, category_href)
        category_list.append(category_url)


def get_books_url():
    read_page(category_url)
    while True:
        books = soup.find_all('h3')
        for book in books:
            books_href = book.find('a')['href']
            books_url = urljoin(category_url, books_href)
            book_list.append(books_url)
        try:
            find_next = soup.find_all('li', class_='next')[0].find('a')['href']
            next_url = urljoin(category_url, find_next)
            print(next_url)
            read_page(next_url)
        except IndexError:
            break


def create_dir():
    cat_exists = exists(f'data/script_3/{category}')
    cat_img_exists = exists(f'data/script_3/{category}/images')
    if not cat_exists:
        os.mkdir(f'data/script_3/{category}')
    if not cat_img_exists:
        os.mkdir(f'data/script_3/{category}/images')


def write_info_csv():
    with open(f'data/script_3/{category}/{category}.csv', 'a', encoding='utf-8-sig') as csv_file:
        file_empty = os.stat(f'data/script_3/{category}/{category}.csv').st_size == 0
        writer = csv.DictWriter(csv_file, output)
        if file_empty:
            writer.writeheader()
        writer.writerow(output)


def get_image():
    download_image = requests.get(image_url).content
    with open(f'data/script_3/{category}/images/{title}.jpg', 'wb') as jpg_file:
        jpg_file.write(download_image)


# --- MAIN ---

get_category_url()
print(category_list)
print(len(category_list))

for cats in category_list:
    read_page(cats)
    get_books_url()
    print(book_list)
    print(len(book_list))

    for item in book_list:
        # ---SCRAPING---
        read_page(item)

        title = soup.find('h1').text.replace('/', '-')

        category = soup.find_all('a')[3].text

        review_rating = soup.find_all('p', class_='star-rating')[0].get('class')[1]
        review_rating = w2n.word_to_num(review_rating)

        product_description = soup.find_all('article')[0].find_all('p')[3].text

        upc = soup.find_all('td')[0].text

        price_tax_excl = soup.find_all('td')[2].text

        price_tax_incl = soup.find_all('td')[3].text

        number_available = soup.find_all('td')[5].text
        number_available = re.sub("[^0-9]", "", number_available)

        image_url = soup.find('img')['src']
        image_url = urljoin(item, image_url)

        url = item

        # ---BOOK INFO TO DICTIONARY---
        output = {variable: eval(variable) for variable in ['title',
                                                            'category',
                                                            'review_rating',
                                                            'product_description',
                                                            'upc',
                                                            'price_tax_excl',
                                                            'price_tax_incl',
                                                            'number_available',
                                                            'image_url',
                                                            'url']}

        # ---WRITING CSV & GETTIN IMAGE---
        create_dir()

        write_info_csv()

        get_image()


print(time.time() - start_time, "seconds")
