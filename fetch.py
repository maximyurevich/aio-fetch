"""Aiohttp fetch function"""
import asyncio
import logging
from sys import platform
from aiohttp.client import ClientSession


logging.basicConfig(level=logging.INFO)


async def fetch(client: ClientSession, url: str) -> str:
    """aiohttp fetch function

    Args:
        client (ClientSession)
        url (str)

    Returns:
        [str]: response text
    """
    async with client.get(url) as res:
        assert res.status == 200
        return await res.text()

async def main():
    """main function"""
    async with ClientSession() as session:
        url = 'https://go.nasa.gov/3GFJChb'
        html = await fetch(session, url)
        logging.info(html)

if __name__ == '__main__':
    if platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
