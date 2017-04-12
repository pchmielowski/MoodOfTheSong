import os
import wave

import numpy as np


class FileSignal:
    def __init__(self, path, mongo, grid):
        assert os.path.isfile(path)
        self.path = path
        self.db = mongo
        self.fs = grid

    def value(self):
        file = wave.open(self.path, 'r')
        content = np.fromstring(file.readframes(-1), 'Int16')
        file.close()
        # self.__cache(content)
        return content

    # @todo #0 create caching decorator:

    # value(self):
    #   ret = origin.value()
    #   self.__cache(ret)
    #   return ret
    def __cache(self, content):
        self.db.meta.insert_one(
            {"path": self.path,
             "signal": self.fs.put(content.tobytes())})
