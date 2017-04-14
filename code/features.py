import librosa
import numpy as np


def random(y):
    return np.random.random(1)


def five(y):
    return np.array([5000])


class Features:
    features = {
        "zero crossing rate": librosa.feature.zero_crossing_rate,
        "spectral rolloff": librosa.feature.spectral_rolloff,
        "spectral bandwidth": librosa.feature.spectral_bandwidth,
        "spectral centroid": librosa.feature.spectral_centroid,
        "spectral contrast": librosa.feature.spectral_contrast,
        "random": random,
        "five": five
    }
