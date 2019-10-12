import json
from application.data_provider.database_pd.model import Model

class HistogramModel(Model):
    def insert(self, key, data): 
        meta_data = {'data': json.dumps(data)}
        super().insert({**key, **meta_data})
    
    def get_histogram_by_key(self, key):
        data = super().find_one(key)
        if data is not None:
            return json.loads(data.get('data', None))
        return