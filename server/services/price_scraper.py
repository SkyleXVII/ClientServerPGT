# services/price_scraper.py

import aiohttp
from bs4 import BeautifulSoup

class GamePriceService:
    @staticmethod
    async def scrape_store(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.text()
                soup = BeautifulSoup(content, 'html.parser')
                # Парсинг данных
                return parsed_data