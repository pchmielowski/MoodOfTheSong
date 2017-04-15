from calculatingSummary import CalculatingSummary
from signals_factory import SignalsFactory
from scatter import Scatter
from text import Text

if __name__ == "__main__":
    # MongoSummary(feature="random")
    CalculatingSummary(
        feature="zero crossing rate",
        factory=SignalsFactory(use_db=False)).scatter()
