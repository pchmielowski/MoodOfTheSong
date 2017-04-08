import os
import wave

import gridfs
import matplotlib.pyplot as plt
import numpy as np
import scipy
from pymongo import MongoClient

from Summary import Summary

db = MongoClient().gridfs_signals
fs = gridfs.GridFS(db)


# @todo #0 each class in another file

class Directory:
    def __init__(self, directory):
        self.directory = directory

    def signals(self):
        return map(
            lambda file: Signal(self.directory + file).value(),
            os.listdir(self.directory)
        )


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


def plot(data):
    plt.figure(1)
    plt.plot(data)
    plt.show()
    plt.interactive(False)


class Stats:
    def __init__(self, directory, transform):
        self.directory = directory
        self.transform = transform

    def value(self):
        rates = list(
            map(
                lambda data: self.transform(data).mean(),
                self.directory.signals()
            )
        )
        return {
            "mean": scipy.mean(rates),
            "std": scipy.std(rates)
        }


def random(y):
    return np.random.random(1)


class Graph:
    @staticmethod
    def show(means, deviations):
        plt.bar(
            [0, 1, 2, 3],
            means,
            .2,
            yerr=deviations,
            ecolor='k')
        plt.show()


if __name__ == "__main__":
    Summary("random").show_on(Graph())
