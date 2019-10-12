
import json
from flask import Response
class ResponseProvider(Response):
    def __init__(self, data):
        super().__init__(json.dumps({
            'data': data
        }))