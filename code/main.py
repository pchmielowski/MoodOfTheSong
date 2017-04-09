import gridfs
import pymongo

from calculatingSummary import CalculatingSummary
from filesignals import FileSignals, DbSignals


class SignalsFactory:
    def __init__(self, use_db):
        self.use_db = use_db
        self.db = pymongo.MongoClient().signals

    def create(self, path):
        # @todo #0 reverse if
        if not self.use_db:
            return FileSignals(path,
                               self.db,
                               gridfs.GridFS(self.db))
        else:
            return DbSignals(path,
                             self.db,
                             gridfs.GridFS(self.db))


class Text:
    def show(self, m, d):
        print("Means:      {}".format(m))
        print("Deviations: {}".format(d))


if __name__ == "__main__":
    # MongoSummary(feature="random")
    CalculatingSummary(
        feature="zero crossing rate",
        factory=SignalsFactory(use_db=True)).show_on(Text())
