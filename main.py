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

import streamlit as st
import pandas as pd
import random

# Page settings
st.set_page_config(page_title="Quote Generator", page_icon="💬", layout="centered")
st.title("💬 Quote Generator")

# Load quotes from CSV just once
@st.cache_data
def load_quotes():
    return pd.read_csv("quotes.csv")

# Load and store in session
if 'quotes' not in st.session_state:
    st.session_state.quotes = load_quotes()

# Show a new quote when button is pressed
if st.button("Show me a quote"):
    random_row = st.session_state.quotes.sample(1).iloc[0]
    st.session_state.current_quote = random_row

# Display current quote
if 'current_quote' in st.session_state:
    quote = st.session_state.current_quote
    st.markdown(f"""
    <div style="font-size: 24px; font-style: italic; margin-bottom: 10px;">
        "{quote['quote']}"
    </div>
    <div style="font-size: 20px; text-align: right;">
        — <strong>{quote['author']}</strong>
    </div>
    """, unsafe_allow_html=True)
