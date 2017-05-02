import numpy as np
from matplotlib import pyplot as plt


# @todo #0 choose better name


class Scatter:
    def __init__(self, moods):
        assert len(moods) == 4
        self.moods = moods

    def show(self, name):
        # @todo #0 refactor
        colors = ['red', 'blue', 'green', 'magenta']
        i = 0

        # from mpl_toolkits.mplot3d import Axes3D
        # import pylab
        # fig = pylab.figure()
        # ax = Axes3D(fig)

        for mood in self.moods:
            print("Mood no. {}".format(i))
            assert i < 4
            # if i == 2:  # debug
            #     break
            print("vectors = mood.vectors()")
            vectors = mood.vectors()
            print("asarray = np.asarray(vectors)")
            asarray = np.asarray(vectors)
            print("var = asarray.T")
            var = asarray.T
            print(var.shape)
            print(var.dtype)
            plt.scatter(
                # ax.scatter(
                var[0,],
                var[1,],
                # z,
                color=colors[i],
                marker='+')
            i += 1

        plt.savefig(name)
        plt.show()
        # import pickle
        # pickle.dump(fig, open('plot3d.fig.pickle', 'wb'))
        # plt.close()
