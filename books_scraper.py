import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt

url = 'http://books.toscrape.com/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

books = soup.find_all('article', class_='product_pod')

titles = []
prices = []

with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Price', 'Availability'])

    for book in books:
        title = book.h3.a['title']
        price_text = book.find('p', class_='price_color').text.strip()  # baş/son boşlukları kaldır
        price = float(price_text.replace('£', '').replace('Â', ''))  # £ ve olası karakterleri temizle
        availability = book.find('p', class_='instock availability').text.strip()

        titles.append(title)
        prices.append(price)

        writer.writerow([title, price, availability])

print("Data has been saved to books.csv.")

# Plot price distribution
plt.figure(figsize=(10, 6))
plt.barh(titles, prices, color='skyblue')
plt.xlabel('Price (£)')
plt.title('Books Price Distribution')
plt.tight_layout()
plt.show()
