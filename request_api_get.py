import asyncio
from aiohttp import request

async def get_task(url):
    async with request('GET', url) as response:
        list= await response.json()
        for responses in list:
            print(responses)

async def main(url):
    await asyncio.gather(get_task(url))
    print("main")

if __name__ == "__main__":
    print("hi") 
    asyncio.run(main("http://127.0.0.1:8000/api/product/"))
    print("how are you")
print("helllo")                