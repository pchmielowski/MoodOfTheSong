import librosa
import numpy as np


def random(y):
    return np.random.random(1)


class Features:
    features = {
        "zero crossing rate": librosa.feature.zero_crossing_rate,
        "random": random
    }
