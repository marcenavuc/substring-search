from collections import namedtuple
from algorithms import ALGORITHMS
from algorithms.Algorithm import Algorithm
import pkg_resources
import unittest


TestData = namedtuple('TestData', ['name', 'text', 'substring', 'expected'])


def load_texts(file_name):
    with pkg_resources.resource_stream(__name__, file_name) as file:
        return file.read().decode('utf-8')


LOREM_IPSUM = load_texts('lorem_ipsum.txt')

TESTS = [
    TestData('begin', LOREM_IPSUM, 'Lorem ipsum', [0]),
    TestData('end', LOREM_IPSUM, 'Nullam', [193]),
    TestData('e', LOREM_IPSUM, 'e',
              [3, 24, 32, 35, 51, 58, 61, 64, 68, 71, 74, 81, 93, 130, 170]),
]


class TestAlgorithms(unittest.TestCase):

    # Алгоритм должен наследоваться от класса Algorithm
    def test_algorithm_is_algorithm(self):
        for algorithm in ALGORITHMS:
            self.assertIsInstance(algorithm(), Algorithm)

    def test_usual(self):
        for test in TESTS:
            for algorithm in ALGORITHMS:
                actual = algorithm.findall(test.substring, test.text)
                self.assertEqual(actual, test.expected,
                                 f'Error in {test.name}')

    def test_print(self):
        for algorithm in ALGORITHMS:
            print(algorithm.name())


if __name__ == '__main__':
    unittest.main()
