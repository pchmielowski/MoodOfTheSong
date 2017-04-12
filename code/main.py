from calculatingSummary import CalculatingSummary
from signals_factory import SignalsFactory
from text import Text

if __name__ == "__main__":
    # MongoSummary(feature="random")
    CalculatingSummary(
        feature="zero crossing rate",
        factory=SignalsFactory(use_db=True)).show_on(Text())
