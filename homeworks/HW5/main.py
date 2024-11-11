import aiohttp
import asyncio
import httpx
import time
from modules.isDigit import getNumber
from modules.check_url import check_url

urls=[]




print("welcome to the best IDM of your life")
user_connections = getNumber("how many connections you want to create for each file? ")


while True:
    user_request = input("please eneter the url you wnat to download from: ")
    goodUrl = check_url(user_request)
    
    if goodUrl:
        urls.append(user_request)
    else:
        print("bad url")

    finish = input("you have more urls (Y/n)? ")
    if finish.lower() == "n":
        break
    continue

user_choice = input("do you want to download multiple files at the same time (Y/n)? ")
if user_choice.lower() == "y":
    pass

async def fetchUrl(session , url , start_byte , end_byte):
    header = {'Range' : f'bytes={start_byte}-{end_byte}'}
    async with session.get(url , headers = header) as response:
        return await response.text()
    
async def main(url , number_of_connections):
    async with aiohttp.ClientSession() as session:
        start = time.time()
        size = int((await session.head(url)).headers['Content-Length'])
        chunk = size // number_of_connections

        tasks = []
        for i in range (number_of_connections):
            start_byte = i * chunk
            end_byte = ((i + 1) * chunk ) -1
            if i == number_of_connections -1:
                end_byte = size - 1
            tasks.append(fetchUrl(session , url , start_byte , end_byte))

        results = await asyncio.gather(*tasks)
        for url , content in zip(urls , results):
            print(f'fetched {len(content)} from {url}')
            end = time.time()
            print(end - start)
    


if __name__ == "__main__":
    for url in urls:
        asyncio.run(main(url , user_connections))
