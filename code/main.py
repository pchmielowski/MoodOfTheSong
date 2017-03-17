import wave
import matplotlib.pyplot as plt
import numpy as np
from os import listdir


def signal(path):
    file = wave.open(path, 'r')
    content = np.fromstring(file.readframes(-1), 'Int16')
    file.close()
    return content


def plot(data):
    plt.figure(1)
    plt.plot(data)
    plt.show()
    plt.interactive(False)


PATH = '../dataset/emotion-recognition-236f22a6fde0/' \
    + '4. dataset (audio)/Angry_all/'
files = listdir(PATH)
print(files)
plot(signal(PATH + files[0]))
