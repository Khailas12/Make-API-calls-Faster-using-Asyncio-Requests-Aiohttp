# aiohttp is used to build useful libraries built on top of it, and there's a page dedicated to list them: Third-Party libraries. There are also projects that leverage the power of aiohttp to provide end-user tools, like command lines or software with full user interfaces.

import aiohttp as web
import asyncio


async def main():
    async with web.ClientSession() as session:
        async with session.get('http://python.org') as response:
            
            print("Status: ", response.status)
            print("Content-type: ", response.headers['content-type'])
            
            html = await response.text()
            print("Body: ", html[:15], "___")
            
loop = asyncio.get_event_loop()
loop.run_until_complete(main())


async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app)