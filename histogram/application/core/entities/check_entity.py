class CheckEntity(object):
    def __init__(self):
        self.is_ok = False
    
    def ok(self):
        self.is_ok = True
        return self

    def check(self):
        return self.is_ok