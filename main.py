"""Aiohttp fetch function"""
import asyncio
import logging
from aio_fetch import fetch
from aiohttp.client import ClientSession


logging.basicConfig(level=logging.INFO)


async def main():
    """main function"""
    async with ClientSession() as session:
        url = 'https://www.nasa.gov/press-release/nasa-tv-to-air-spacex-cargo-dragon-departure-from-space-station'
        html = await fetch(session, url)
        logging.info(html)

if __name__ == '__main__':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())