import streamlit as st

# Exchange rates dictionary
rates = {'a': 1500, 'b': 2000, 'c': 5500}

st.set_page_config(page_title="Advanced Currency Converter", page_icon="💱", layout="centered")
st.title("💱 Advanced Currency Converter")

# Sidebar inputs for a clean UI
st.sidebar.header("Converter Settings")
currency = st.sidebar.selectbox("Choose currency type:", options=list(rates.keys()), format_func=lambda x: f"Currency {x.upper()}")
amount = st.sidebar.number_input("Enter amount to convert:", min_value=0, step=1, format="%d")

# Button to trigger conversion
if st.sidebar.button("Convert"):
    if amount <= 0:
        st.error("Please enter an amount greater than zero.")
    else:
        result = amount * rates[currency]
        st.success(f"💰 {amount} units of Currency {currency.upper()} = {result:,} Naira")

# Optional: Show exchange rates table
with st.expander("See all exchange rates"):
    st.table({f"Currency {k.upper()}": [v] for k, v in rates.items()})
