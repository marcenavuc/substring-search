import unittest
from benchmark import Benchmark, create_parser, todonext


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
            benchmark.report('test', benchmark.test_time, save=False)

    def test_todonext(self):
        benchmark = Benchmark(1)
        benchmark.save_results('results_time.xlsx', benchmark.test_time)

    def test_create_parser(self):
        create_parser()

    def test_save_report_img(self):
        benchmark = Benchmark(1)
        args = create_parser().parse_args(['1', '--report-img'])
        todonext(benchmark, args)

    def test_save_stat(self):
        benchmark = Benchmark(1)
        args = create_parser().parse_args(['1', '--stat'])
        todonext(benchmark, args)

    def test_save_stat(self):
        benchmark = Benchmark(1)
        args = create_parser().parse_args(['1', '--save-results'])
        todonext(benchmark, args)


if __name__ == '__main__':
    unittest.main()
