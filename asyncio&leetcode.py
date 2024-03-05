import asyncio
import json

async def data_1():
    with open('data1.json', 'r') as file:
        data = json.load(file)
        return data

async def data_2(data):
    with open('data2.json', 'w') as file:
        json.dump(data, file)

async def task1():
    data = await data_1()
    print("Data 1 read:", data)
    return data

async def task2(data):
    await data_2(data)
    print("Data 2 written:", data)

async def main():
    data = await task1()
    await task2(data)

asyncio.run(main())
