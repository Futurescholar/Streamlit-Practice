import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd

base_url = 'http://quotes.toscrape.com/'
url = base_url
all_quotes = []

while True:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    quotes = soup.find_all('div', class_='quote')

    for q in quotes:
        text = q.find('span', class_='text').text.strip()
        author = q.find('small', class_='author').text.strip()
        all_quotes.append({'quote': text, 'author': author})

    next_button = soup.find('li', class_='next')
    if next_button:
        next_page = next_button.a['href']
        url = urljoin(url, next_page)
    else:
        break

    time.sleep(1)

# Save to CSV
df = pd.DataFrame(all_quotes)
df.to_csv('quotes.csv', index=False)
print("Quotes saved to quotes.csv")
