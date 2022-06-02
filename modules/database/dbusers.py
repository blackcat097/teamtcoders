import motor.motor_asyncio

class Database:
    def __init__(self, url, database_name):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(url)
        self.db = self._client[database_name]
        self.col = self.db.users

async def total_users_count(self):
        count = await self.col.count_documents({})
        return count
