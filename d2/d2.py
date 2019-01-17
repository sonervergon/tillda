class DictHash(object):
    def __init__(self, arg):
        self.dict = {}

    def store(self, key, data):
        self.dict[key] = data

    def search(self, search_string):
        return self.dict[search_string]
