import itertools

import sklearn.decomposition

from mongoCache import MongoCache
from normalization import NormalizedVectors, Norms
from scatter import Scatter
from stats import Vectors


class CalculatingSummary:
    def __init__(self, features, factory):
        assert hasattr(features, '__iter__')
        self.features = features
        # @todo #0 compound name: directory_factory
        self.signals_factory = factory

    # @todo #inject scatter
    def scatter(self, name):
        moods = self.__moods()
        norms = Norms.Cached(Norms(moods))
        print("norms calculated in CalculatingSummary")
        normalized = list(map(
            lambda songs: Vectors.Cached(NormalizedVectors(
                songs,
                norms
            )),
            moods
        ))
        print("normalized in CalculatingSummary")
        Scatter(normalized).show(name)

    def __moods(self):
        """:returns list of Vectors"""
        return list(map(
            lambda directory:
            Vectors.Cached(
                Vectors(directory, self.features)),
            map(
                lambda path: self.signals_factory.create(path),
                ['Angry_all/',
                 'Happy_all/',
                 'Relax_all/',
                 'Sad_all/']
            )
        ))

    def __cache(self, stats):
        # @todo #0 save values in { "happy" : value, "sad" : val ... } format
        MongoCache("stats").save(
            {"feature": self.features,
             "stats": list(stats)})

    # @todo #0 move to seperate class
    def __normalize_and_rotate(self, moods):
        vectors = list(itertools.chain.from_iterable(moods))

        norms = CalculatingSummary.__calculate_norms(vectors)
        vectors = CalculatingSummary.__normalize_all(
            vectors,
            norms)

        pca = self.__train_pca(vectors)
        print("variance ratio: {}".format(pca.explained_variance_ratio_))
        moods = list(map(
            lambda mood: CalculatingSummary.__normalize_all(mood, norms),
            moods
        ))
        return self.__rotate(moods, pca)

    def __rotate(self, moods, pca):
        print("len(moods): {}".format(len(moods)))
        vectors = list(map(
            lambda mood: pca.transform(mood),
            moods))
        print(
            "{} x {} of {} x {} of {} x {}".format(
                len(vectors),
                type(vectors[0]),
                len(vectors[0]),
                type(vectors[0][0]),
                len(vectors[0][0]),
                type(vectors[0][0][0]),
            ))
        return vectors

    def __train_pca(self, vectors):
        pca = sklearn.decomposition.PCA(n_components=3)
        pca.fit(vectors)
        return pca
