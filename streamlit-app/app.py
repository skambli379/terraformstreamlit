# import streamlit as st

# st.title("Hello, Streamlit!")
# st.write("This is a simple Streamlit application.")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title('Cryptocurrency Data Visualizer')

# Fetch data from an API (e.g., CoinGecko API)
def fetch_data():
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart'
    params = {'vs_currency': 'usd', 'days': '30'}
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

# Load data
df = fetch_data()

# Plot the data
st.line_chart(df.set_index('timestamp')['price'])

# Optionally, add other visualizations or interactive elements