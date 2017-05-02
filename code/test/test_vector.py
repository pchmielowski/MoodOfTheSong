from unittest import TestCase

import numpy as np

from stats import Vectors


class TestVector(TestCase):
    def test_empty_transform_list(self):
        sut = Vectors.Vector([])

        result = sut(np.asarray([1, 2, 3]))

        self.assertEqual(result, [])

    def test_one_transform(self):
        class MeanOfTwoTimes:
            def __call__(self, x):
                return [np.multiply(x, 2).mean()]

        sut = Vectors.Vector([
            MeanOfTwoTimes()
        ])

        result = sut(np.asarray([3, 5, 7]))

        self.assertEqual(result, [10.0])

    def test_transform_returning_more_than_one(self):
        class TwoTimes:
            def __call__(self, x):
                return np.multiply(x, 2)

        sut = Vectors.Vector([
            TwoTimes()
        ])

        result = sut(np.asarray([3, 5, 7]))

        np.testing.assert_array_equal(result, [6, 10, 14])

    def test_two_transforms(self):
        class One:
            def __call__(self, x):
                return [1]

        class Twos:
            def __call__(self, x):
                return [2, 2]

        class Threes:
            def __call__(self, x):
                return [3, 3, 3]

        sut = Vectors.Vector([
            One(),
            Twos(),
            Threes(),
        ])

        result = sut(np.asarray([3, 5, 7]))

        self.assertEqual(result, [1, 2, 2, 3, 3, 3])
