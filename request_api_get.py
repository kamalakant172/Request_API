import asyncio
from aiohttp import request
from getinfo import get_url

async def get_task(url):
    async with request('GET', url) as response:
        list= await response.text()
        print(list)
        print(response.url)
       

async def main(url):
    data= await asyncio.gather(get_task(url))
    return data
print("main")

if __name__ == "__main__":
    print("hi") 
    asyncio.run(main(get_url()))
    print("how are you")
print("hello")
