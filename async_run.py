import asyncio
import aiohttp
import time
import os


# https://www.alphavantage.co/support/#api-key  -> get api_key from here
api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}"

symbols = ["GOOG", "APPL", "TSLA", "MCFT", "GOOG", "APPL", "TSLA", "MCFT", "GOOG", "APPL", "TSLA", "MCFT"]
results = []

start = time.time()

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
async def get_symbols():
    async with aiohttp.ClientSession() as session:    # this will automatically close the session insead of writing session.close()
        for symbol in symbols:
            print("Working on a symbol {}".format(symbol))
            response = await session.get(url.format(symbol, api_key, ssl=False))
            results.append(await response.json())
            # Without await, it wouldn't return anything. So it is important in here.
            # coroutine function may be defined with the async def statement and may contain await, async for, and async with keywords


asyncio.run(get_symbols())  # same as the below one
# loop = asyncio.get_event_loop() # event loop for checking things in there 
# loop.run_until_complete(get_symbols())
# loop.close()


end = time.time()
total_time = end - start


print(
    "Time taken is {} seconds to make {} API calls".format(total_time, len(symbols))
)
print("Done!")
