import json
from application.data_provider.database_pd.model import Model


class HistogramModel(Model):
    async def insert(self, key, data):
        meta_data = {'data': json.dumps(data)}
        await super().insert({**key, **meta_data})

    async def get_histogram_by_key(self, key):
        data = await super().find_one(key)
        if data is not None:
            return json.loads(data.get('data', None))
        return
