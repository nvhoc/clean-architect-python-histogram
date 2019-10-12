import config

from pymongo import MongoClient
from application.lib import singleton, dyn_import_class
from application.data_provider.const import database as db_const

@singleton
class DatabaseProvider(object):
    def __init__(self):
        dbc = config.of().get('db', db_const.DEFAULT_CONFIG)
        host = dbc.get('host')
        port = int(dbc.get('port'))
        database = dbc.get('database')
        self.conn = MongoClient(host=host, port=port)[database]
    
    
    def get_model(self, collection_name: str):
        module_path = 'application.data_provider.database_pd.model.{}_model'.format(collection_name)
        class_name = '{}Model'.format(collection_name.title())
        return dyn_import_class(module_path, class_name)(collection_name)
