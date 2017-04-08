from matplotlib import pyplot as plt


class Graph:
    @staticmethod
    def show(means, deviations):
        plt.bar(
            [0, 1, 2, 3],
            means,
            .2,
            yerr=deviations,
            ecolor='k')
        plt.show()