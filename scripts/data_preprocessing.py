import requests
import time
import json
from datetime import datetime


# API_KEY 
TOKEN = 'ALPHA_VANTAGE_API_KEY'
ticker = 'AAPL'

# Function to fetch historical APPLE stock data.
def fetch_historical_weather(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={TOKEN}&outputsize=full'
    print(url)
    headers = {'token': TOKEN}
    response = requests.get(url, headers=headers)
    return response.json()

# Fetch data
data = fetch_historical_weather(ticker)

# Write data to JSON file
with open('./full_stock_data.json', 'w') as f:
    json.dump(data, f, indent=4)



#### FILTER DATA ####
# Load data from JSON file
with open('full_stock_data.json', 'r') as f:
    data = json.load(f)

# Get the current date and the date 15 years ago
start_date = datetime.strptime('2008-06-10', '%Y-%m-%d')

# Filter data to include only dates from the past 15 years
filtered_data = {
    "Meta Data": data["Meta Data"],
    "Time Series (Daily)": {
        date: values for date, values in data["Time Series (Daily)"].items()
        if datetime.strptime(date, '%Y-%m-%d') >= start_date
    }
}

# Write filtered data to a new JSON file
with open('filtered_stock_data.json', 'w') as f:
    json.dump(filtered_data, f, indent=4)



