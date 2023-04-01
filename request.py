import asyncio
from aiohttp import ClientSession

async def get_task(session,url):
        async with session.get(url) as resp:
            response= await resp.json()
            for responses in response:
                print(responses)

async def post_task(session,url, payload):
     async with session.post(url, data=payload) as respo:
          create= await respo.json()
          for create_product in create:
               print(create_product)
                            
async def main(url):
    payload_data= {
         'product_name': 'Mobile123224a', 'price': 3200664567, 'desc': 'Samsung Mobile123',
         
         'category': 'http://127.0.0.1:8000/api/category/3/'
    }
    async with ClientSession() as session:
        task=[]
        task.append(asyncio.ensure_future(get_task(session, url)))
        task.append(asyncio.ensure_future(post_task(session, url, payload=payload_data)))

        main_func= await asyncio.gather(*task)
        for main_function in main_func:
             print(main_function)
        
if __name__ == "__main__":
    asyncio.run(main("http://127.0.0.1:8000/api/product/")) 

                                           