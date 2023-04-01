import asyncio
from aiohttp import request


async def get_task(url):
    async with request('GET', url) as response:
        list= await response.json()
        for responses in list:
            print(responses)
        
async def post_task(url, payload):
    async with request('POST', url, data=payload) as respo:
        create= await respo.json()
        for create_product in create:
            print(create_product)           
                            
async def main(url):
    payload_data= {
         'product_name': 'AAAMobile1232322A24a', 'price': 3200664567, 'desc': 'Samsung Mobile123',
         'category': 'http://127.0.0.1:8000/api/category/3/'
    }
    main_func= await asyncio.gather(get_task(url), post_task(url, payload=payload_data))
    for main_function in main_func:
        print(main_function)
        
if __name__ == "__main__":
    asyncio.run(main("http://127.0.0.1:8000/api/product/"))
print("hi")
                                           