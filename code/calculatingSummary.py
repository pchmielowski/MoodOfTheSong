from features import Features
from mongoCache import MongoCache
from stats import Stats


class CalculatingSummary:
    def __init__(self, feature, factory):
        if not Features.features.__contains__(feature):
            raise Exception('There is no feature called: ' + feature)
        self.feature = feature
        # @todo #0 compound name: directory_factory
        self.signals_factory = factory

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
            Stats(
                directory,
                Features.features[self.feature]).value(),
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
            {"feature": self.feature,
             "stats": list(stats)})
