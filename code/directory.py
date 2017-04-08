import os

from Signal import Signal


class Directory:
    def __init__(self, directory):
        self.directory = \
            '../dataset/emotion-recognition-236f22a6fde0/4. dataset (audio)/' \
            + directory

    def signals(self):
        return map(
            lambda file: Signal(self.directory + file).value(),
            os.listdir(self.directory)
        )