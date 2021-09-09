#asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.


from typing_extensions import runtime
import requests
import asyncio
import time
import datetime

# async def main():
#     print("hello...")
#     await asyncio.sleep(1)
#     print("...world")

# asyncio.run(main())

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
    
    
# A coroutine function may be defined with the async def statement, and may contain await, async for, and async with keywords 
async def main():   
    print(f"started at {time.strftime('%X')}")
    await say_after(1, 'hello')
    await say_after(2, 'world')
    print(f"Finished at {time.strftime('%X')}")
    
    task1 = asyncio.create_task(
        say_after(1, "hello")
    )
    task2 = asyncio.create_task(
        say_after(2, "world")
    )
    
    print(f"\nstarted at {time.strftime('%X')}")
    await task1
    await task2
    print(f"Finished at {time.strftime('%X')}")

asyncio.run(main())
    

# There are three main types of awaitable objects: coroutines, Tasks, and Futures.

async def nested():
    return 42

async def main_two():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested()
    print(await nested()) # here the await helps to run that and prints 42

asyncio.run(main_two())


# Tasks -> used to schedule coroutines concurrently.
async def main_tasks():
    task = asyncio.create_task(nested())
    
    await task

asyncio.run(main_tasks())


# Future -> special low-level awaitable object that represents an eventual result of an asynchronous operation.
# When a Future object is awaited it means that the coroutine will wait until the Future is resolved in some other place.



# coroutine displaying the current date every second for 5 seconds
async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0    # it loops 5 times
    
    while True:
        print(f'\n\n Display Date: {datetime.datetime.now()}')    
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1) 

asyncio.run(display_date())