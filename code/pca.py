import sklearn


class PcaModel:
    def __init__(self, moods, components=3):
        self.pca = sklearn.decomposition.PCA(components)
        all_vectors = []
        for mood in moods:
            for v in mood.vectors():
                all_vectors.append(v)
        self.pca.fit(all_vectors)

    def rotate(self, vectors):
        self.pca.transform(vectors)
