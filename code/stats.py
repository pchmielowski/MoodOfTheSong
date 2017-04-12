import multiprocessing
import scipy


# Statistics per mood
class Stats:
    def __init__(self, directory, transform):
        self.directory = directory
        self.transform = transform

    def value(self):
        vectors = Vectors(self.directory, [self.transform]).vectors()
        return {
            "mean": scipy.mean(vectors),
            "std": scipy.std(vectors)
        }


class Vectors:
    class Calculate:
        def __init__(self, transform):
            self.transform = transform

        def __call__(self, data):
            return self.transform(data).mean()

    def __init__(self, directory, transforms):
        self.directory = directory
        self.transforms = transforms

    def vectors(self):
        # @todo #0 handle more transforms
        vectors = list(
            multiprocessing.Pool().imap_unordered(
                Vectors.Calculate(self.transforms[0]),
                self.directory.signals()
            )
        )
        assert vectors is not None
        for rate in vectors:
            assert rate is not None
        return vectors
