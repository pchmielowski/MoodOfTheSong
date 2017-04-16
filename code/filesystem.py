import wave
import os

import numpy as np


class FileSystem:
    def __init__(self):
        self.contents = {}

    def content(self, path):
        assert os.path.isfile(path)
        # if path in self.contents:
        #     return self.contents[path]
        file = wave.open(path, 'r')
        content = np.fromstring(file.readframes(-1), 'Int16')
        file.close()
        # self.contents[path] = content
        return content

    __instance = None

    @staticmethod
    def instance():
        if not FileSystem.__instance:
            FileSystem.__instance = FileSystem()
        return FileSystem.__instance
