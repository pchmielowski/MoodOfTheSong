import multiprocessing

from features import Features
from mongoCache import MongoCache
from stats import Stats
from directory import Directory


class CalculatingSummary:
    class Calculate(object):
        def __init__(self, feature):
            self.feature = feature

        def __call__(self, directory):
            return Stats(
                directory,
                Features.features[self.feature]).value()

    def __init__(self, feature):
        self.feature = feature
        CalculatingSummary.feature = feature
        if not Features.features.__contains__(feature):
            raise Exception('There is no feature called: ' + feature)

    def show_on(self, graph):
        stats = self.__calculate()
        self.__cache(stats)
        means = []
        deviations = []
        for stat in stats:
            means.append(stat["mean"])
            deviations.append(stat["std"])
        graph.show(means, deviations)

    def __calculate(self):
        return multiprocessing.Pool().map(
            CalculatingSummary.Calculate(self.feature),
            map(
                lambda path: Directory(path),
                ['Angry_all/',
                 'Happy_all/',
                 'Relax_all/',
                 'Sad_all/']
            )
        )

    def __cache(self, stats):
        # @todo #0 save values in { "happy" : value, "sad" : val ... } format
        MongoCache("stats").save(
            {"feature": self.feature,
             "stats": stats})
