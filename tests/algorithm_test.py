from collections import namedtuple
from algorithms.Algorithm import Algorithm
from algorithms.Automat import Automat
from algorithms.BoyerMoore import BoyerMooreSearch
from algorithms.Bruteforce import BruteForce
from algorithms.HashSearch import RabinKarpSearch
import pkg_resources
import unittest

ALGORITHMS = [
    BruteForce(),
    RabinKarpSearch(),
    Automat(),
    BoyerMooreSearch(),
]
TestData = namedtuple('TestData', ['name', 'text', 'substring', 'expected'])


def load_texts(file_name):
    with pkg_resources.resource_stream(__name__, file_name) as file:
        return file.read().decode('utf-8')


class TestAlgorithms(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.LOREM_IPSUM = load_texts('lorem_ipsum.txt')
        self.TESTS = [
            TestData('begin', self.LOREM_IPSUM, 'Lorem ipsum', [0]),
            TestData('end', self.LOREM_IPSUM, 'Nullam', [193]),
            TestData('e', self.LOREM_IPSUM, 'e',
                     [3, 24, 32, 35, 51, 58, 61, 64, 68, 71, 74, 81, 93, 130,
                      170]),
        ]

    # Алгоритм должен наследоваться от класса Algorithm
    def test_algorithm_is_algorithm(self):
        for algorithm in ALGORITHMS:
            self.assertIsInstance(algorithm, Algorithm)

    def test_usual(self):
        for test in self.TESTS:
            for algorithm in ALGORITHMS:
                actual = algorithm.findall(test.substring, test.text)
                self.assertEqual(actual, test.expected,
                                 f'Error in {test.name}')


if __name__ == '__main__':
    unittest.main()
