import requests
from bs4 import BeautifulSoup
from word2number import w2n

base_url = 'http://books.toscrape.com/'
url = 'http://books.toscrape.com/catalogue/sharp-objects_997/index.html'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find('h1').text

category = soup.find_all('a')[3].text

review_rating = soup.find_all('p', class_='star-rating')[0].get('class')[1]
review_rating = w2n.word_to_num(review_rating)

product_description = soup.find_all('meta')[2]

upc = soup.find_all('td')[0].text

price_tax_excl = soup.find_all('td')[2].text

price_tax_incl = soup.find_all('td')[3].text

number_available = soup.find_all('td')[5].text[10:13]

image_url = soup.find('img')['src']
image_url = base_url + image_url


