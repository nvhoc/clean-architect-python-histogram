from heapq import nlargest 
from application.lib import singleton

@singleton
class DictProvider(object):
    def top(self, obj, num):
        if num > len(obj):
            num = len(obj)
        return nlargest(num, obj, key = obj.get) 