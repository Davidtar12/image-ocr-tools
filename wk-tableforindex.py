import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/Nasdaq-100'

# Fetch the webpage
html = requests.get(url).content

# Use pandas to read the tables from the webpage
df_list = pd.read_html(html)

# Specify the index of the table you want to scrape
# Replace 'table_index' with the index number of the table
table_index = 4 # For example, 0 for the first table
try:
    desired_table = df_list[table_index]
    print(desired_table)
except IndexError:
    print(f"Table index {table_index} is out of range. The page might have fewer tables.")

# Optional: Save the table to a CSV file
# desired_table.to_csv('nasdaq_100.csv', index=False)