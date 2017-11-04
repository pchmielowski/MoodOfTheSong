import librosa
import numpy as np


def random(y):
    return np.random.random(1)


def five(y):
    return np.array([5])


class Mean:
    def __init__(self, function):
        self.function = function

    def __call__(self, signal):
        return [self.function(signal).mean()]


class Simple:
    def __init__(self, function):
        self.function = function

    def __call__(self, signal):
        return self.function(signal)


class Features:
    features = [
        Simple(librosa.beat.tempo)
        # Mean(librosa.feature.zero_crossing_rate),
        # Mean(librosa.feature.spectral_rolloff)
        # librosa.feature.spectral_bandwidth,
        # librosa.feature.spectral_centroid,
        # librosa.feature.spectral_contrast,
        # librosa.feature.chroma_cens,
        # librosa.feature.chroma_cqt,
        # librosa.feature.chroma_stft
    ]
