from matplotlib import pyplot as plt


# @todo #0 choose better name
class Scatter:
    def __init__(self, moods):
        # assert len(list(moods)) == 4
        self.moods = moods

    def show(self):
        # @todo #0 refactor
        colors = ['red', 'blue', 'green', 'magenta']
        i = 0
        for mood in self.moods:
            print("Mood no. {}".format(i))
            assert i < 4
            x = []
            y = []
            for vec in mood:
                assert len(vec) == 2
                x.append(vec[0])
                y.append(vec[1])
            plt.scatter(
                x,
                y,
                color=colors[i])
            i += 1

        plt.show()
