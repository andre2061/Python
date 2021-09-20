import requests
from bs4 import BeautifulSoup
import pandas from pd
import csv




base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
base_url.format(2)
for i in range(1,51):
    print(base_url.format(i))
result = requests.get('http://books.toscrape.com/catalogue/page-1.html')

soup = bs4.BeautifulSoup(result.text, 'lxml')

soup
soup.select('.product_pod')
len(soup.select('.product_pod'))
20

soup.select('.product_pod')[0]
output = soup.select('.product_pod')[0]

'star-rating Two' in str(output)
False

type(output)
bs4.element.Tag

output.select('.star-rating.Two')
output.select('.star-rating.Two') == []
output.select('a')[1]['title']
print('My name is {}'.format('Bhavya'))

titles = []

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
for i in range (1,51):
    scrape_url = base_url.format(i)

    result = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            title = book.select('a')[1]['title']
            titles.append(title)
	titles
len(titles)
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
for i in range (1,51):
    scrape_url = base_url.format(i)

    result = requests.get(scrape_url)
    soup = bs4.BeautifulSoup(result.text, 'lxml')
    books = soup.select('.product_pod')

    for book in books:
        if len(book.select('.star-rating.Two')) != 0:
            title = book.select('a')[1]['title']
            print(title)
			