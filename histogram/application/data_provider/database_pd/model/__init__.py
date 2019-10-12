from datetime import datetime 

from pymongo.collection import Collection
from application.data_provider.database_pd import DatabaseProvider
class Model(Collection):
    def __init__(self, name):
        db_provider = DatabaseProvider()
        super().__init__(db_provider.conn, name)
    
    def insert(self, data):
        date_object = {'created': datetime.now(), 'updated': datetime.now()}
        super().insert({**data, **date_object})