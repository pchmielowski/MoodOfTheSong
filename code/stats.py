import multiprocessing
import scipy
import librosa

from features import Features


class Stats:
    '''Statistics per mood'''

    def __init__(self, directory, transform):
        self.directory = directory
        self.transform = transform

    def value(self):
        # @todo #0 let it accept a list of features
        vectors = Vectors(self.directory, [self.transform, Features.features["five"]]).vectors()
        # @todo #0 now it calculates mean/std of whole list of lists. let it be feature-wise
        return {
            "mean": scipy.mean(vectors),
            "std": scipy.std(vectors)
        }


class Vectors:
    '''a collection of vectors per mood'''

    class Vector:
        class Feature:
            def __init__(self, signal):
                self.signal = signal

            def __call__(self, transform):
                return transform(self.signal).mean()

        def __init__(self, transforms):
            self.transforms = transforms

        def __call__(self, signal):
            return list(
                map(
                    Vectors.Vector.Feature(signal),
                    self.transforms
                ))

    def __init__(self, directory, transforms):
        self.directory = directory
        self.transforms = transforms

    def vectors(self):
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
