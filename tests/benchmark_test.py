import unittest
from benchmark import Benchmark


class TestUtils(unittest.TestCase):

    def test_correct_init(self):
        for i in range(10):
            Benchmark(i)

    def test_run(self):
        for i in range(10):
            Benchmark(i).run()


if __name__ == '__main__':
    unittest.main()
