import wave
import matplotlib.pyplot as plt
import numpy as np
import librosa
import scipy
import os


class Signals:
    def __init__(self, directory):
        self.directory = directory

    def __signal(self, file):
        file = wave.open(self.directory + file, 'r')
        content = np.fromstring(file.readframes(-1), 'Int16')
        file.close()
        return content

    def values(self):
        return map(
            self.__signal,
            os.listdir(self.directory)
        )


def plot(data):
    plt.figure(1)
    plt.plot(data)
    plt.show()
    plt.interactive(False)


def features(path):
    rates = list(
        map(
            lambda data: librosa.feature.zero_crossing_rate(data).mean(),
            Signals(path).values())
    )
    return [
        scipy.mean(rate),
        scipy.std(rates)
    ]


PATH = '../dataset/emotion-recognition-236f22a6fde0/4. dataset (audio)/'
MOODS = ['Angry_all/',
         'Happy_all/',
         'Relax_all/',
         'Sad_all/']
for rate in map(
        lambda mood: features(PATH + mood),
        MOODS):
    print(rate)
