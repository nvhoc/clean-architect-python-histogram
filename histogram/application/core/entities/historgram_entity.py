#The Entity is only store text
class HistogramEntity(object):
    def __init__(self, data: dict):
        self.data = data

    def get(self):
        return self.data
