from pymongo import MongoClient


class MongoCache:
    def __init__(self):
        self.mongo = MongoClient('mongodb://localhost:27017/').db.stats

    def save(self, means, deviations):
        self.mongo.insert_one({"means": means,
                               "deviations": deviations})

    def read(self):
        return self.mongo.find_one()
