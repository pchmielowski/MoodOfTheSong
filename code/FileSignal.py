import os


class FileSignal:
    def __init__(self, path, system):
        assert os.path.isfile(path)
        self.path = path
        self.system = system

    def value(self):
        content = self.system.content(self.path)
        return content

    '''
    @todo #0 create caching decorator:
     value(self):
     ret = origin.value()
     self.db.meta.insert_one(
     {"path": self.path,
     "signal": self.fs.put(ret.tobytes())})
     return ret
    '''
