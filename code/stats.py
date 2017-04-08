import scipy


class Stats:
    def __init__(self, directory, transform):
        self.directory = directory
        self.transform = transform

    def value(self):
        rates = list(
            map(
                lambda data: self.transform(data).mean(),
                self.directory.signals()
            )
        )
        return {
            "mean": scipy.mean(rates),
            "std": scipy.std(rates)
        }
