"""
Program that uses the dual moving average crossover to decide when to buy and sell stocks
"""

import json
import quandl
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# Stock symbol can be changed to use on different companies
STOCK_SYMBOL = "AAPL"

# Authenticating quandl API
with open('config.json') as config_file:
    keys = json.load(config_file)
api_key = keys['api_key']
quandl.ApiConfig.api_key = api_key

# Loading data
dataset = quandl.get(f"WIKI/{STOCK_SYMBOL}", start_date='2010-01-01', end_date='2015-01-01')
print('First 5 rows')
print(dataset.head(), end='\n\n\n')

# Visualise the data
plt.figure(figsize=(12, 6))
plt.plot(dataset['Adj. Close'], label="AAPL")
plt.title("Apple adjusted close price history")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price USD ($)")
plt.legend(loc='upper left')
plt.show()

# Create simple moving average with 30 day window
SMA_30 = pd.DataFrame()
SMA_30['Adj Close Price'] = dataset['Adj. Close'].rolling(window=30).mean()
print("First 5 rows of 30 day moving average")
print(SMA_30.head(), end='\n\n\n')

# Create simple moving average with 100 day window
SMA_100 = pd.DataFrame()
SMA_100['Adj Close Price'] = dataset['Adj. Close'].rolling(window=100).mean()
print("First 5 rows of 100 day moving average")
print(SMA_30.head(), end='\n\n\n')

# Visualise dat with moving averages
plt.figure(figsize=(12, 6))
plt.plot(dataset['Adj. Close'], label="AAPL")
plt.plot(SMA_30['Adj Close Price'], label="SMA30")
plt.plot(SMA_100['Adj Close Price'], label="SMA100")
plt.title("Apple adjusted close price history")
plt.xlabel("Date")
plt.ylabel("Adjusted Close Price USD ($)")
plt.legend(loc='upper left')
plt.show()

# Create new dataframe to store the original data and movinng averages
data = pd.DataFrame()
data[STOCK_SYMBOL] = dataset['Adj. Close']
data['SMA_30'] = SMA_30['Adj Close Price']
data['SMA_100'] = SMA_100['Adj Close Price']
print("First 5 rows of data")
print(data.head(), end='\n\n\n')
