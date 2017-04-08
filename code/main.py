import os
import wave

import librosa
import matplotlib.pyplot as plt
import numpy as np
import scipy

from MongoCache import MongoCache
import multiprocessing
from pymongo import MongoClient
import gridfs

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

        # @todo #0 split into 3 classes: readFromFile, savetoDB, readFromDb
        fs_id = fs.put(content.tobytes())
        db.meta.insert_one({"path": self.path, "signal": fs_id})

        return np.frombuffer(
            fs.get(
                db.meta.find_one(
                    {"path": self.path}
                )["signal"]).read(), dtype='Int16')


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


class Summary:
    PATH = '../dataset/emotion-recognition-236f22a6fde0/4. dataset (audio)/'
    features = {
        "zero crossing rate": librosa.feature.zero_crossing_rate
    }

    def __init__(self, feature):
        self.feature = feature
        if not Summary.features.__contains__(feature):
            raise Exception('There is no feature called: ' + feature)

    # @todo #0 rename
    def foo(self, mood):
        return Stats(
            Directory(Summary.PATH + mood),
            Summary.features[self.feature]).value()

    def show_on(self, graph):
        moods = [
            'Angry_all/',
            'Happy_all/',
            'Relax_all/',
            'Sad_all/']
        stats = multiprocessing.Pool().map(
            Summary.foo,
            moods)
        means = []
        deviations = []
        for stat in stats:
            means.append(stat["mean"])
            deviations.append(stat["std"])
        # @todo #0 split into 3 classes: calculating, saving and reading ones
        # @todo #0 save values in { "happy" : value, "sad" : val ... } format
        MongoCache("stats").save(
            {"feature": self.feature,
             "means": means,
             "deviations": deviations
             })
        from_db = MongoCache("stats").read()
        graph.show(from_db["means"], from_db["deviations"])


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
    Summary("zero crossing rate").show_on(Graph())
