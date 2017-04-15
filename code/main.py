import librosa

from calculatingSummary import CalculatingSummary
from features import Features, random, five
from signals_factory import SignalsFactory
from scatter import Scatter
from text import Text
import itertools
import time

if __name__ == "__main__":
    # MongoSummary(feature="random")
    for i in itertools.combinations(Features.features, 2):
        print(time.time())
        names = list(map(lambda x: x.__name__, i))
        png_name = "{}-{}.png".format(names[0], names[1])
        CalculatingSummary(
            features=[
                i[0],
                i[1]
            ],
            factory=SignalsFactory(use_db=False)).scatter(png_name)
