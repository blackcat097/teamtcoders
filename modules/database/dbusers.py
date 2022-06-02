import motor.motor_asyncio



async def total_users_count(self):
        count = await self.col.count_documents({})
        return count
