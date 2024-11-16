import aiohttp
import asyncio
import time
from modules.isDigit import getNumber
from modules.check_url import check_url
from modules.type import select_file_type

urls=[]

print("welcome to the best IDM of your life")
user_connections = getNumber("how many connections you want to create for each file? ")


while True:
    user_request = input("please eneter the url you wnat to download from: ")
    goodUrl = check_url(user_request)
    
    if goodUrl:
        user_filename = input("plese enter a file name for the downloading file: ")
        urls.append([user_request , user_filename])
        
    else:
        print("bad url")

    finish = input("you have more urls (Y/n)? ")
    if finish.lower() == "n":
        break
    continue

user_choice = input("do you want to download multiple files at the same time (Y/n)? ")


async def fetchUrl(session , url , start_byte , end_byte):
    header = {'Range' : f'bytes={start_byte}-{end_byte}'}
    async with session.get(url , headers = header) as response:
        return await response.read()
        
    
async def main(url , number_of_connections , filename , job):
    print(f"start job{job}")
    async with aiohttp.ClientSession() as session:
        start = time.time()
        size = int((await session.head(url)).headers['Content-Length'])
        content_type = (await session.head(url)).headers['Content-Type']
        extention = select_file_type(content_type)
        print(content_type)
        chunk = size // number_of_connections

        filename = filename + extention

        tasks = []
        for i in range (number_of_connections):
            start_byte = i * chunk
            end_byte = ((i + 1) * chunk ) -1
            if i == number_of_connections -1:
                end_byte = size - 1
            tasks.append(fetchUrl(session , url , start_byte , end_byte))

        results = await asyncio.gather(*tasks)
        with open('./downloads/' + filename , 'w+') as file:
            for task in results:
                    file.write(task.decode('utf-8'))
            
        end = time.time()
        print(end - start)
        print(f"end job{job}")
           
async def handleMultiFile():
    job = 1
    tasks = []
    for url , filename in urls:
        tasks.append(main(url , user_connections , filename , job))
        job += 1
    results = await asyncio.gather(*tasks)
    return results





if __name__ == "__main__":
    if user_choice.lower() == "y":
       asyncio.run(handleMultiFile())
    else:
        job = 1
        for url in urls:
            asyncio.run(main(url[0] , user_connections , url[1] , job))
            job += 1
            
        print("finisehd all")