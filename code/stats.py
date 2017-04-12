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


class Do:
    def __init__(self, signal):
        self.signal = signal

    def __call__(self, transform):
        # try without self
        return transform(self.signal).mean()


class Vectors:
    class Vector:
        def __init__(self, transforms):
            self.transforms = transforms

        def __call__(self, signal):
            # todo return vector
            return list(
                map(
                    Do(signal),
                    self.transforms
                ))

    def __init__(self, directory, transforms):
        self.directory = directory
        self.transforms = transforms

    def vectors(self):
        # @todo #0 handle more transforms
        vectors = list(
            multiprocessing.Pool().imap_unordered(
                Vectors.Vector(self.transforms),
                self.directory.signals()
            )
        )
        assert vectors is not None
        for rate in vectors:
            assert rate is not None
        return vectors
