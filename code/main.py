from calculatingSummary import CalculatingSummary
from features import Features
from signals_factory import SignalsFactory

if __name__ == "__main__":
    CalculatingSummary(
        features=Features.features,
        factory=SignalsFactory(use_db=False)) \
        .scatter("after_pca.png")

    # scatter 3d
    # normalize b4 pca
