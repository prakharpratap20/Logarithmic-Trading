import yfinance as yf
import pandas as pd

# Define the stock symbol and the date range you're interested in
stock_symbol = "AAPL"  # Example: Apple Inc.
start_date = "2000-01-01"
end_date = "2023-11-08"

# Use the Yahoo Finance API to get historical data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Save the data to a CSV file
csv_file = f"{stock_symbol}.csv"
stock_data.to_csv(csv_file)

# Print the data (optional)
print(stock_data)

print(f"Data saved to {csv_file}")
