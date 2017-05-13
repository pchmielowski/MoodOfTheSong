import numpy as np
import scipy


class NormalizedVectors:
    def __init__(self, origin, norms):
        assert hasattr(origin, 'vectors')
        self.origin = origin
        assert hasattr(norms, 'norms')
        self.norms = norms

    def vectors(self):
        return np.asarray(list(map(
            lambda song: self.__normalize(song, self.norms),
            self.origin.vectors())))

    @staticmethod
    def __normalize(song, norms):
        assert len(song) == len(norms.norms())
        return np.divide(song, norms.norms())


class Norms:
    def __init__(self, moods):
        self.moods = moods

    def norms(self):
        # return [100.3, 98.0]
        print("starting calculating norms")

        all_vectors = []
        for mood in self.moods:
            for v in mood.vectors():
                all_vectors.append(v)

        print("map flattened")
        return [scipy.linalg.norm(vec) for vec in np.asarray(all_vectors).T]

    class Cached:
        def __init__(self, origin):
            assert hasattr(origin, 'norms')
            self.cached = origin.norms()

        def norms(self):
            return self.cached
