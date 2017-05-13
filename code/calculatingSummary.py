from mongoCache import MongoCache
from normalization import NormalizedVectors, Norms
from pca import PcaModel
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
        print("starting to calculate PCA")
        model = PcaModel(normalized, 2)
        print("PCA model trained")
        rotated = list(map(
            lambda mood: model.rotate(mood),
            moods))
        print("all vectors rotated")
        Scatter(rotated).show(name)

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
