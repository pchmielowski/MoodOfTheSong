import os
import wave

import numpy as np


class FileSystem:
    def __init__(self):
        self.contents = {}

    def content(self, path):
        assert os.path.isfile(path)
        # if path in self.contents:
        #     return self.contents[path]
        file = wave.open(path, 'r')
        content = np.fromstring(file.readframes(-1), "Int16")
        # import plot
        # plot.plot(content)
        # file.close()
        # import sys
        # sys.exit("Error message")
        self.contents[path] = content
        return content

    __instance = None

    @staticmethod
    def instance():
        if not FileSystem.__instance:
            FileSystem.__instance = FileSystem()
        return FileSystem.__instance
