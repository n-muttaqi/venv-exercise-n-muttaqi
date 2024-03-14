import requests
import numpy as np
import pandas as pd

def fetch_data():
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['bpi']
    else:
        print("Failed to fetch data")
        return None

def process_data(data):
    currencies = list(data.keys())
    values = list(data.values())
    return currencies, values

def display_data(currencies, values):
    df = pd.DataFrame({'Currency': currencies, 'Value': values})
    print(df)

def main():
    data = fetch_data()
    if data:
        currencies, values = process_data(data)
        display_data(currencies, values)

if __name__ == "__main__":
    main()
