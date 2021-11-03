import requests
from bs4 import BeautifulSoup
from word2number import w2n
import csv
import time
import re

start_time = time.time()

base_url = 'http://books.toscrape.com/'
url = 'http://books.toscrape.com/catalogue/ready-player-one_209/index.html'

print(time.time() - start_time, "seconds")
