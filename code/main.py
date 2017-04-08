import gridfs
import matplotlib.pyplot as plt
from pymongo import MongoClient

from graph import Graph
from mongoSummary import MongoSummary

db = MongoClient().gridfs_signals
fs = gridfs.GridFS(db)


# @todo #0 each class in another file


def plot(data):
    plt.figure(1)
    plt.plot(data)
    plt.show()
    plt.interactive(False)


if __name__ == "__main__":
    MongoSummary("random2").show_on(Graph())
