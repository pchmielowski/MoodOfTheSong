from graph import Graph
from mongoSummary import MongoSummary

if __name__ == "__main__":
    MongoSummary(feature="random2").show_on(Graph())
