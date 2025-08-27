import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Quote Generator", page_icon="💬", layout="centered")
st.title("💬 Quote Generator")

@st.cache_data
def load_quotes():
    return pd.read_csv("quotes.csv")

if 'quotes' not in st.session_state:
    st.session_state.quotes = load_quotes()

if st.button("Show me a quote"):
    random_row = st.session_state.quotes.sample(1).iloc[0]
    st.session_state.current_quote = random_row

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
