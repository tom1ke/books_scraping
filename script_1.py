import requests
from bs4 import BeautifulSoup
from word2number import w2n
import csv
import time
import re
import os
from os.path import exists
from urllib.parse import urljoin

# ---SETUP---
start_time = time.time()

base_url = 'http://books.toscrape.com/'
url = 'http://books.toscrape.com/catalogue/ready-player-one_209/index.html'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# ---FUNCTIONS---


def create_dir():
    data_exists = exists('data')
    script_dir_exists = exists('data/script_1')
    img_exists = exists('data/script_1/images')
    if not data_exists:
        os.mkdir('data')
    if not script_dir_exists:
        os.mkdir('data/script_1')
    if not img_exists:
        os.mkdir('data/script_1/images')


def write_info_csv():
    with open(f'data/script_1/{title}.csv', 'w', encoding='utf-8-sig') as csv_file:
        writer = csv.DictWriter(csv_file, output)
        writer.writeheader()
        writer.writerow(output)


def get_image():
    download_image = requests.get(image_url).content
    with open(f'data/script_1/images/{title}.jpg', 'wb') as jpg_file:
        jpg_file.write(download_image)


# ---SCRAPING---
title = soup.find('h1').text

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
image_url = urljoin(base_url, image_url)

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
