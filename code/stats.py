import multiprocessing
import scipy


class Do:
    def __init__(self, transform):
        self.transform = transform

    def __call__(self, data):
        return self.transform(data).mean()


class Stats:
    def __init__(self, directory, transform):
        self.directory = directory
        self.transform = transform

    def value(self):
        rates = list(
            multiprocessing.Pool().imap_unordered(
                Do(self.transform),
                self.directory.signals()
            )
        )
        assert rates is not None
        for rate in rates:
            assert rate is not None
        return {
            "mean": scipy.mean(rates),
            "std": scipy.std(rates)
        }
