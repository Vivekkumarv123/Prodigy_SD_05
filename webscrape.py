import requests
from bs4 import BeautifulSoup
import csv

url = 'http://books.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all('article', class_='product_pod')

with open('books.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Price', 'Rating'])

    for product in products:
        try:
            name = product.h3.a['title']
            price = product.select_one('.price_color').text.strip()
            rating_class = product.select_one('.star-rating')['class'][1]
            rating = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}[rating_class]

            writer.writerow([name, price, rating])
        except Exception as e:
            print(f"Error extracting data from product: {e}")