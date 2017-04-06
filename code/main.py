import os
import wave

import librosa
import matplotlib.pyplot as plt
import numpy as np
import scipy

from MongoCache import MongoCache
import multiprocessing


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


class Comparision:
    PATH = '../dataset/emotion-recognition-236f22a6fde0/4. dataset (audio)/'

    @staticmethod
    def foo(mood):
        return Stats(
            Directory(Comparision.PATH + mood),
            librosa.feature.zero_crossing_rate).value()

    @staticmethod
    def show_on(graph):
        moods = [
            'Angry_all/',
            'Happy_all/',
            'Relax_all/',
            'Sad_all/']
        stats = multiprocessing.Pool().map(
            Comparision.foo,
            moods)
        means = []
        deviations = []
        for stat in stats:
            means.append(stat["mean"])
            deviations.append(stat["std"])
        MongoCache().save(means, deviations)
        from_db = MongoCache().read()
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
    Comparision().show_on(Graph())
