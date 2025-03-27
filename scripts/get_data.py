import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

import matplotlib.pyplot as plt

def get_nvidia_stock_data(period="1y", interval="1d"):
    """
    Get NVIDIA stock data from Yahoo Finance
    
    Args:
        period (str): Time period to get data for (e.g., "1d", "1mo", "1y", "5y", "max")
        interval (str): Data interval (e.g., "1m", "1h", "1d", "1wk", "1mo")
        
    Returns:
        pandas.DataFrame: DataFrame with the stock data
    """
    # Get NVIDIA stock data (ticker: NVDA)
    ticker = "NVDA"
    stock_data = yf.download(ticker, period=period, interval=interval)
    
    print(f"Downloaded {len(stock_data)} records of NVIDIA stock data")
    return stock_data

def save_close_price(stock_data, output_file="nvidia_close_price.csv"):
    """
    Extract and save the closing price to a CSV file
    
    Args:
        stock_data (pandas.DataFrame): DataFrame with stock data
        output_file (str): Name of the output file
    """
    # Extract close price
    close_price = stock_data[["Close"]].copy()
    
    # Save to CSV
    close_price.to_csv(output_file)
    print(f"Saved closing price data to {output_file}")
    return close_price

def plot_close_price(close_price):
    """Plot the closing price"""
    plt.figure(figsize=(12, 6))
    plt.plot(close_price.index, close_price["Close"])
    plt.title("NVIDIA Stock Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("nvidia_close_price.png")
    plt.show()

if __name__ == "__main__":
    # Get stock data for the past 5 years with daily intervals
    stock_data = get_nvidia_stock_data(period="max", interval="1d")
    
    # Print the head of the data
    print("\nFirst 5 rows of the data:")
    print(stock_data.head())
    
    # Save and plot close price
    close_price = save_close_price(stock_data)
    plot_close_price(close_price)