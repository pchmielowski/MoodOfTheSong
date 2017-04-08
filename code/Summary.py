import multiprocessing

import librosa

from MongoCache import MongoCache
from main import Stats, Directory, random


class Summary:
    class Calculate(object):
        def __init__(self, feature):
            self.feature = feature

        def __call__(self, mood):
            return Stats(
                Directory(Summary.PATH + mood),
                Summary.features[self.feature]).value()

    feature = None
    PATH = '../dataset/emotion-recognition-236f22a6fde0/4. dataset (audio)/'
    features = {
        "zero crossing rate": librosa.feature.zero_crossing_rate,
        "random": random
    }

    def __init__(self, feature):
        self.feature = feature
        Summary.feature = feature
        if not Summary.features.__contains__(feature):
            raise Exception('There is no feature called: ' + feature)

    def show_on(self, graph):
        moods = [
            'Angry_all/',
            'Happy_all/',
            'Relax_all/',
            'Sad_all/']
        stats = multiprocessing.Pool().map(
            Summary.Calculate(self.feature),
            moods)
        # @todo #0 split into 3 classes: calculating, saving and reading ones
        # @todo #0 save values in { "happy" : value, "sad" : val ... } format
        MongoCache("stats").save(
            {"feature": self.feature,
             "stats": stats})

        means = []
        deviations = []
        for stat in MongoCache("stats").read({"feature": self.feature})["stats"]:
            means.append(stat["mean"])
            deviations.append(stat["std"])

        graph.show(means, deviations)