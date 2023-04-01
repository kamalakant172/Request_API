import asyncio
from aiohttp import request

async def post_task(url, payload):
    async with request('POST', url, data=payload) as respo:
        create= await respo.json()
        for create_product in create:
            print(create_product)  

async def main(url):
    payload_data= {
         'product_name': 'BBBBAAAMobile1232322A24a', 'price': 3200664567, 'desc': 'Samsung Mobile123',
         'category': 'http://127.0.0.1:8000/api/category/3/'
    }
    await asyncio.gather(post_task(url, payload=payload_data)) 
    print("main")

if __name__ == "__main__":
    asyncio.run(main("http://127.0.0.1:8000/api/product/"))
print("hi")               