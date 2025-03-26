# utils/cache.py

import redis.asyncio as redis

class CacheManager:
    def __init__(self):
        self.redis = redis.Redis(host='localhost', port=6379)

    async def get(self, key):
        return await self.redis.get(key)

    async def set(self, key, value, ttl=3600):
        await self.redis.setex(key, ttl, value)