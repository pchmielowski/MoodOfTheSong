import gridfs
import pymongo

from filesignals import DbSignals, FileSignals


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
