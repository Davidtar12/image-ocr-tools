import requests
import pandas as pd
from io import StringIO

def extract_tables_to_text(url):
    # Headers to mimic a web browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # Fetch the webpage content
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error fetching the website:", response.status_code, response.reason)
        return

    # Use StringIO to handle the HTML content
    html_content = StringIO(response.text)

    # Use pandas to extract tables
    tables = pd.read_html(html_content)

    # Save each table to a text file
    for i, table in enumerate(tables):
        filename = f"table_{i}.txt"
        table.to_csv(filename, sep='\t', index=False)
        print(f"Table {i} saved as {filename}")

# URL of the website
url = "https://www.slickcharts.com/nasdaq100"
extract_tables_to_text(url)