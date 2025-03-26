# server/utils/threading.py

from concurrent.futures import ThreadPoolExecutor
import asyncio

class AsyncThreadPool:
    def __init__(self, max_workers=10):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    async def run(self, func, *args, **kwargs):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(self.executor, func, *args, **kwargs)

# Инициализация в main.py
thread_pool = AsyncThreadPool(max_workers=20)