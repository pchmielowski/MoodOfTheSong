import itertools
import time

from calculatingSummary import CalculatingSummary
from features import Features
from signals_factory import SignalsFactory

if __name__ == "__main__":
    # MongoSummary(feature="random")
    for combination in itertools.combinations(Features.features, 2):
        print(time.time())
        names = list(map(lambda x: x.__name__, combination))
        CalculatingSummary(
            features=[
                combination[0],
                combination[1]
            ],
            factory=SignalsFactory(use_db=False)) \
            .scatter("{}-{}.png".format(names[0], names[1]))
