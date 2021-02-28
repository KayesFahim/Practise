import requests
from bs4 import BeautifulSoup


res = requests.get('https://www.daraz.com.bd/')
soup = BeautifulSoup(res.text, 'html.parser')

print(soup.find_all('div'))