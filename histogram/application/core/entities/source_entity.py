from application.core.const import source as source_const
from application.core.exceptions.source import SourceNotSupport, SourceParamRequired
 
class SourceEntity(object):
    def __init__(self, data_source: str, data_format: str, params: dict):
        self.data_source = data_source
        self.data_format = data_format
        self.params = params
        self.validation()

    def get_key(self):
        key = source_const.SOURCE_KEY.get(self.data_source)
        if not key:
            raise SourceNotSupport()
        return key
    
    def validation(self):
        required_params = source_const.SOURCE_REQUIRED.get(self.data_source)
        if not required_params:
            raise SourceNotSupport()
        for param_key in required_params:
            if not self.params.get(param_key):
                raise SourceParamRequired(param_key)