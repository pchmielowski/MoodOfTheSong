import multiprocessing

import scipy


class Stats:
    """Statistics per mood"""

    def __init__(self, directory, transforms):
        self.directory = directory
        assert hasattr(transforms, '__iter__'), "Features are not iterable"
        self.transforms = transforms

    def value(self):
        # @todo #0 let it accept a list of features
        vectors = Vectors(self.directory, self.transforms).vectors()
        '''
        @todo #0 now it calculates mean/std of whole list of lists.
         let it be feature-wise
        '''
        return {
            "mean": scipy.mean(vectors),
            "std": scipy.std(vectors)
        }


class Vectors:
    """a collection of vectors per mood"""

    class Vector:

        def __init__(self, features):
            self.features = features

        def __call__(self, signal):
            vector = []
            for feature in self.features:
                out = feature(signal)
                assert out.ndim == 1
                for o in out:
                    vector.append(o)
            return vector

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

    class Cached:
        def __init__(self, origin):
            assert hasattr(origin, 'vectors')
            print(end="caching... ")
            self.cached = origin.vectors()
            print("cached")

        def vectors(self):
            return self.cached
