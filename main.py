"""Aiohttp fetch function"""
import asyncio
import logging
from fetch import fetch
from aiohttp.client import ClientSession


logging.basicConfig(level=logging.INFO)


async def main():
    """main function"""
    async with ClientSession() as session:
        url = 'https://go.nasa.gov/3GFJChb'
        html = await fetch(session, url)
        logging.info(html)

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
