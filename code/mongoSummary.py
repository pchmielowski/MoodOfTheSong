from features import Features
from mongoCache import MongoCache


class MongoSummary:
    def __init__(self, feature):
        self.feature = feature
        if not Features.features.__contains__(feature):
            raise Exception('There is no feature called: ' + feature)

    def show_on(self, graph):
        means = []
        deviations = []
        obj = MongoCache("stats").read({"feature": self.feature})
        if not obj:
            raise Exception("Summary for {} is not present in database"
                            .format(self.feature))
        for stat in obj["stats"]:
            means.append(stat["mean"])
            deviations.append(stat["std"])
        graph.show(means, deviations)
