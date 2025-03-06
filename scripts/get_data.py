import yfinance as yf

# Define the Bitcoin ticker symbol
btc = yf.Ticker("BTC-USD")

df = btc.history(start="2014-09-17", end="2024-12-31")

df = df[["Close"]]

# Save it as a CSV file
df.to_csv("bitcoin_data.csv")

# Display the first few rows
print(df.head())
