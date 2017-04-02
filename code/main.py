import wave
import matplotlib.pyplot as plt
import numpy as np
import librosa
import scipy
import os


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
    def __init__(self, path, transform):
        self.path = path
        self.transform = transform

    def value(self):
        assert os.path.isdir(self.path)
        rates = list(
            map(
                lambda data: self.transform(data).mean(),
                Directory(self.path).signals()
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
    lambda m: Stats(PATH + m, librosa.feature.zero_crossing_rate).value(),
    MOODS)
for stat in stats:
    means.append(stat["mean"])
    deviations.append(stat["std"])

plt.bar([0, 1, 2, 3], means, .2, yerr=deviations, ecolor='k')
plt.show()
