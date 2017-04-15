from features import Features
from mongoCache import MongoCache
from scatter import Scatter
from stats import Stats


class CalculatingSummary:
    def __init__(self, features, factory):
        assert hasattr(features, '__iter__')
        self.features = features
        # @todo #0 compound name: directory_factory
        self.signals_factory = factory

    # @todo #inject scatter
    def scatter(self, name):
        Scatter(self.__calculate()).show(name)

    def show_on(self, graph):
        stats = self.__calculate()
        # @todo #0 uncomment following

        # self.__cache(stats)
        means = []
        deviations = []
        for stat in stats:
            means.append(stat["mean"])
            deviations.append(stat["std"])
        graph.show(means, deviations)

    def __calculate(self):
        return map(
            lambda directory:
            Stats(directory, self.features).vectors(),
            map(
                lambda path: self.signals_factory.create(path),
                ['Angry_all/',
                 'Happy_all/',
                 'Relax_all/',
                 'Sad_all/']
            )
        )

    def __cache(self, stats):
        # @todo #0 save values in { "happy" : value, "sad" : val ... } format
        MongoCache("stats").save(
            {"feature": self.features,
             "stats": list(stats)})
