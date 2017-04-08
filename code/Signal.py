import os
import wave

import numpy as np


class Signal:
    def __init__(self, path):
        assert os.path.isfile(path)
        self.path = path

    def value(self):
        file = wave.open(self.path, 'r')
        content = np.fromstring(file.readframes(-1), 'Int16')
        file.close()
        return content
        # @todo #0 split into 3 classes: readFromFile, savetoDB, readFromDb
        # fs_id = fs.put(content.tobytes())
        # db.meta.insert_one({"path": self.path, "signal": fs_id})
        #
        # return np.frombuffer(
        #     fs.get(
        #         db.meta.find_one(
        #             {"path": self.path}
        #         )["signal"]).read(), dtype='Int16')
