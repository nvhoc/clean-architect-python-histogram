from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorCollection as Collection
from application.data_provider.database_pd import DatabaseProvider


class Model(Collection):
    def __init__(self, name):
        db_provider = DatabaseProvider()
        super().__init__(db_provider.conn, name)

    async def insert(self, data):
        date_object = {'created': datetime.now(), 'updated': datetime.now()}
        await super().insert_one({**data, **date_object})
