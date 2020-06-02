from collections import namedtuple
import unittest
from pkg_resources import resource_stream
from algorithms import ALGORITHMS
from algorithms.algorithm import Algorithm
import io


TestData = namedtuple('TestData', ['name', 'text', 'substring', 'expected'])


def load_texts(filename):
    with resource_stream(__name__, filename) as file:
        return file.read().decode('utf-8')


def load_answers(filename):
    return list(map(int, load_texts(filename).split()))


LOREM_IPSUM = load_texts('test texts/lorem_ipsum.txt')
CORONA = load_texts('test texts/coronavirus.txt')
DON = load_texts('test texts/tihii_don_tom_1.txt')
ANSWER_HUTOR = load_answers('test answers/Hutor_answer.txt')
ANSWER_DAD = load_answers('test answers/Dad_answer.txt')

TESTS = [
    TestData('begin', LOREM_IPSUM, 'Lorem ipsum', [0]),
    TestData('end', LOREM_IPSUM, 'Nullam', [193]),
    TestData('e', LOREM_IPSUM, 'e',
             [3, 24, 32, 35, 51, 58, 61, 64, 68, 71, 74, 81, 93, 130, 170]),
    TestData('хутор', DON, 'хутор', ANSWER_HUTOR),
    TestData('отец', DON, 'отец', ANSWER_DAD),
    TestData('corona', CORONA, 'ACAATTAATTGCCAGGAACCTAA', [28553])
]


class TestAlgorithms(unittest.TestCase):

    # Алгоритм должен наследоваться от класса Algorithm
    def test_algorithm_is_algorithm(self):
        for algorithm in ALGORITHMS:
            self.assertIsInstance(algorithm(), Algorithm)

    def test_usual(self):
        for test in TESTS:
            for alg in ALGORITHMS:
                actual = alg.findall(test.substring, test.text)
                self.assertEqual(actual, test.expected,
                                 f'Error in {test.name} with {alg.name()}')

    def test_big_file_corona(self):
        path = 'test texts/coronavirus.txt'
        for alg in ALGORITHMS:
            with resource_stream(__name__, path) as file:
                text_io = io.StringIO(file.read().decode('utf-8'))
                actual = alg.big_findall(text_io, 'ACAATTAATTGCCAGGAACCTAA')
                self.assertEqual(actual, [28553], f'Error in {alg}')


if __name__ == '__main__':
    unittest.main()
