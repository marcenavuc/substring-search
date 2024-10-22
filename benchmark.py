from tests.algorithm_test import TESTS
from algorithms import ALGORITHMS
from timeit import timeit
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from memory_profiler import memory_usage
import argparse


class Benchmark:

    def __init__(self, n_times=100):
        self.tests = TESTS
        self.n_times = n_times

        self.test_time = {}
        self.test_mem = {}
        for test in self.tests:
            self.test_time[test.name] = {alg.name(): [] for alg in ALGORITHMS}
            self.test_mem[test.name] = {alg.name(): [] for alg in ALGORITHMS}

    @staticmethod
    def permutation(a, b):
        return zip(a * len(b), b * len(a))

    def run(self):
        start_mem = np.mean(memory_usage())
        execute = 'alg.search(test.substring, test.text)'
        for test, alg in Benchmark.permutation(TESTS, ALGORITHMS):
            memory_expression = (alg.search, (test.substring, test.text))
            for i in range(self.n_times):
                self.test_time[test.name][alg.name()].append(
                    timeit(execute, globals=locals(), number=1))
                self.test_mem[test.name][alg.name()].append(
                    max(memory_usage(memory_expression)) - start_mem)

    def save_results(self, table_name, samples, func=lambda table: table):
        writer = pd.ExcelWriter(table_name)
        columns = [alg.name() for alg in ALGORITHMS]
        for test in self.tests:
            test_table = pd.DataFrame(samples[test.name], columns=columns)
            func(test_table).to_excel(writer, sheet_name=test.name)

        writer.save()

    def report(self, name, samples, pow=1e5, save=True):
        data = self.test_time
        figure, axises = plt.subplots(len(data), figsize=(15, 30))
        for i, test in enumerate(data):
            for alg in data[test]:
                x_arr = range(len(samples[test][alg]))
                y_arr = list(map(lambda x: x * pow, samples[test][alg]))

                axises[i].scatter(x_arr, y_arr, label=alg)
                axises[i].set_title(test)
                axises[i].set_xlabel('runs')
                axises[i].set_ylabel('time powed %s' % pow)
                axises[i].legend()
        if save:
            figure.savefig(name, format='png')


def create_parser():
    parser = argparse.ArgumentParser(description='Simple benchmark for '
                                                 'substring searching '
                                                 'algorithms')
    parser.add_argument('N', metavar='N_times', type=int, help='an integer of '
                                                               'times to run '
                                                               'tests')
    parser.add_argument('--report-img', '-r', dest='is_report',
                        action='store_true',
                        help='makes report of tests in report.png')
    parser.add_argument('--save-results', '-s', dest='is_save',
                        action='store_true',
                        help='save results in results.xlsx')
    parser.add_argument('--stat', dest='is_stat',
                        action='store_true',
                        help='save some statistic in stat.xlsx')
    return parser


def todonext(benchmark, args):
    if args.is_save:
        benchmark.save_results('results_time.xlsx', benchmark.test_time)
        benchmark.save_results('results_mem.xlsx', benchmark.test_mem)
    if args.is_stat:
        benchmark.save_results('stat_time.xlsx',
                               benchmark.test_time,
                               func=lambda table: table.describe())
        benchmark.save_results('stat_mem.xlsx',
                               benchmark.test_mem,
                               func=lambda table: table.describe())
    if args.is_report:
        benchmark.report('results_time.png', benchmark.test_time)
        benchmark.report('results_mem.png', benchmark.test_mem, pow=1)


if __name__ == '__main__':
    args = create_parser().parse_args()
    benchmark = Benchmark(args.N)
    benchmark.run()
    todonext(benchmark, args)

