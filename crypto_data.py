import requests
import pandas as pd
from openpyxl import Workbook
import time

# Function to fetch live cryptocurrency data
def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
    }
    response = requests.get(url, params=params)
    return pd.DataFrame(response.json())

# Initialize Excel file (create a blank Excel file with headers)
def create_excel_file():
    df = pd.DataFrame(columns=["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"])
    # Using 'openpyxl' engine to save as .xlsx format
    with pd.ExcelWriter("crypto_data.xlsx", engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Live Data")

# Create the initial Excel file
create_excel_file()

# Main loop to fetch and update data every 5 minutes
while True:
    # Fetch the live data
    data = fetch_crypto_data()
    df = data[["name", "symbol", "current_price", "market_cap", "total_volume", "price_change_percentage_24h"]]

    # Open the existing file and write the updated data to it
    with pd.ExcelWriter("crypto_data.xlsx", mode="a", engine="openpyxl", if_sheet_exists="replace") as writer:
        df.to_excel(writer, index=False, sheet_name="Live Data")

    print("Data updated in Excel.")
    time.sleep(300)  # Wait for 5 minutes before updating again
