from bs4 import BeautifulSoup
import requests

url = 'https://habr.com/ru/articles/'
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html')

links = soup.find_all('a')

for link in links:
    print(link)

