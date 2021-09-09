import asyncio
import requests
import os

api_key = os.getenv('ALPHADVANTAGE_API_KEY')
url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}"

symbols = ["GOOG", "APPL", "TSLA", "MCFT"]
results = []


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
for symbol in symbols:
    print("Working on a symbol {}".format(symbol))
    response = requests.get(url.format(symbol, api_key))
    results.append(response.json())
    
print("Done")