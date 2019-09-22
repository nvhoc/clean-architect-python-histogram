class Config(object):
    def __init__(self, cfg):
        self.cfg = cfg

    def _get(self, key):
        keys = key.split('.')
        ptr = self.cfg
        for k in keys:
            ptr = ptr.get(k, None)
            if not type(ptr) is dict:
                return ptr
        return ptr  
    def get(self, key, default_value = None):
        value = self._get(key)
        if value is None:
            return default_value
        return value
       
