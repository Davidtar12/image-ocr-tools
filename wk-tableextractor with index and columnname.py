import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Nasdaq-100'

# Fetch the webpage
html = requests.get(url).content

# Use pandas to read the tables from the webpage
df_list = pd.read_html(html)

# Find the correct table. Since the structure might vary, let's look for the table with 'Ticker' in its columns
tickers_table = None
for df in df_list:
    if 'Ticker' in df.columns:
        tickers_table = df
        break

if tickers_table is not None:
    # Extract the column with tickers
    tickers = tickers_table['Ticker']
    print(tickers)
else:
    print("No table with 'Ticker' column found.")