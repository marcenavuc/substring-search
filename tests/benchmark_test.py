import unittest
from benchmark import Benchmark


class TestUtils(unittest.TestCase):

    def test_correct_init(self):
        for i in range(10):
            Benchmark(i)

    def test_run(self):
        for i in range(10):
            Benchmark(i).run()

    def test_report_image(self):
        for i in range(5):
            benchmark = Benchmark(1)
            benchmark.report('test', benchmark.test_time)


if __name__ == '__main__':
    unittest.main()
