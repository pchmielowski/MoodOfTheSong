import wave
import matplotlib.pyplot as plt
import numpy as np
import librosa
import scipy
import os
from pymongo import MongoClient


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


PATH = '../dataset/emotion-recognition-236f22a6fde0/4. dataset (audio)/'
MOODS = ['Angry_all/',
         'Happy_all/',
         'Relax_all/',
         'Sad_all/']
means = []
deviations = []
stats = map(
    lambda m: Stats(
        Directory(PATH + m),
        librosa.feature.zero_crossing_rate).value(),
    MOODS)
for stat in stats:
    means.append(stat["mean"])
    deviations.append(stat["std"])

mongo = MongoClient('mongodb://localhost:27017/').db.stats


def save(means, deviations):
    mongo.insert_one({"means": means,
                      "deviations": deviations})


def read():
    return mongo.find_one()


save(means, deviations)
from_db = read()
plt.bar([0, 1, 2, 3], from_db["means"], .2, yerr=from_db["deviations"], ecolor='k')
plt.show()
