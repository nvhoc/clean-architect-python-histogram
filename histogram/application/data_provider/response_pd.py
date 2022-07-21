import json

from application.lib import singleton


@singleton
class ResponseProvider:

    def json(self, data):
        return json.dumps({
            "data": data,
        })