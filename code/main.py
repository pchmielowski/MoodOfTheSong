import gridfs
import pymongo

from calculatingSummary import CalculatingSummary
from filesignals import FileSignals, DbSignals


class SignalsFactory:
    def __init__(self, use_db):
        self.use_db = use_db
        self.db = pymongo.MongoClient().signals
        self.fs = gridfs.GridFS(self.db)

    def create(self, path):
        if self.use_db:
            return DbSignals(path,
                             self.db,
                             self.fs)
        return FileSignals(path,
                           self.db,
                           self.fs)


class Text:
    def show(self, m, d):
        print("Means:      {}".format(m))
        print("Deviations: {}".format(d))


if __name__ == "__main__":
    # MongoSummary(feature="random")
    CalculatingSummary(
        feature="zero crossing rate",
        factory=SignalsFactory(use_db=True)).show_on(Text())
