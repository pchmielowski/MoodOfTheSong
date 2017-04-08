from pymongo import MongoClient


class MongoCache:
    def __init__(self, collection):
        self.mongo = MongoClient('mongodb://localhost:27017/').db[collection]

    def save(self, data):
        self.mongo.insert_one(data)

    def read(self):
        return self.mongo.find_one()
