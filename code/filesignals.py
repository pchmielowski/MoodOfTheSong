import os

import numpy as np

from FileSignal import FileSignal
from filesystem import FileSystem


class FileSignals:
    # @todo #0 duplicated ctors
    def __init__(self, directory, db, fs):
        self.directory = \
            '../dataset/emotion-recognition-236f22a6fde0/4. dataset (audio)/' \
            + directory
        self.db = db
        self.fs = fs

    def signals(self):
        return map(
            lambda file:
            FileSignal(self.directory + file, FileSystem.instance()).value(),
            os.listdir(self.directory)
        )


class DbSignals:
    def __init__(self, directory, db, fs):
        self.directory = \
            '../dataset/emotion-recognition-236f22a6fde0/4. dataset (audio)/' \
            + directory
        self.db = db
        self.fs = fs

    class Do:
        def __init__(self, directory, db, fs):
            self.directory = directory
            self.db = db
            self.fs = fs

        def __call__(self, file):
            one = self.db.meta.find_one({"path": self.directory + file})
            if not one:
                raise Exception("There is no data for file {} in db.".format(
                    self.directory + file
                ))
            return np.frombuffer(
                self.fs.get(
                    one["signal"]).read(), dtype='Int16')

    def signals(self):
        # @todo #0 try paraller here
        return map(
            DbSignals.Do(self.directory, self.db, self.fs),
            os.listdir(self.directory)
        )
