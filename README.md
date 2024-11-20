Crypto-Analysis

This repository contains a Python script and supporting files for analyzing cryptocurrency data. The data is fetched using the CoinGecko API and saved into an Excel file for further analysis.

Features

	•	Fetches real-time cryptocurrency data (top 50 cryptocurrencies by market cap).
	•	Saves data into an Excel file (crypto_data.xlsx) with the following columns:
	•	Name: Name of the cryptocurrency (e.g., Bitcoin, Ethereum).
	•	Symbol: Short symbol (e.g., BTC, ETH).
	•	Current Price: Latest price in USD.
	•	Market Cap: Total market capitalization.
	•	Total Volume: 24-hour trading volume.
	•	24-Hour Price Change: Percentage change in price over the last 24 hours.
	•	Automatically updates the data every 5 minutes.

 How to Run the Script

	1.	Clone the Repository:
 
  git clone https://github.com/YourGitHubUsername/Crypto-Analysis.git
  cd Crypto-Analysis

	2.	Install Python and Required Libraries:
Make sure Python 3.6 or later is installed on your system. Then, install the following libraries:

          pip install requests pandas openpyxl
          
3.	Run the Script:
Execute the Python script to fetch cryptocurrency data and save it to an Excel file:

python3 crypto_data.py

.	Check the Generated File:
Open the file crypto_data.xlsx in Excel to view the data.

Analysis Tasks

Here are the steps for analyzing the cryptocurrency data:
	1.	Top 5 Cryptocurrencies by Market Cap:
	•	Check the first 5 rows of the Excel file, sorted by the “Market Cap” column.
	2.	Average Price:
	•	Use an Excel formula like =AVERAGE(C2:C51) (replace C2:C51 with the correct range for the “Current Price” column).
	•	Alternatively, calculate the average in Python using:

Python :
         print(df["current_price"].mean())

	3.	Highest/Lowest 24-Hour Price Changes:
	•	Use Excel formulas:
	•	Maximum: =MAX(F2:F51) (replace F2:F51 with the correct range for the “24-Hour Price Change” column).
	•	Minimum: =MIN(F2:F51).
	•	Or calculate in Python:          

  print("Highest 24-hour change:", df["price_change_percentage_24h"].max())
print("Lowest 24-hour change:", df["price_change_percentage_24h"].min())

Files in This Repository

	•	crypto_data.py: Python script to fetch and save cryptocurrency data into an Excel file.
	•	crypto_data.xlsx: The Excel file generated by the script (updated every 5 minutes).

 Requirements

	•	Python 3.6 or later.
	•	Libraries:
	•	requests
	•	pandas
	•	openpyxl

 Author

[ PALLA RAJIV]
Feel free to reach out for any questions or suggestions regarding this project!
