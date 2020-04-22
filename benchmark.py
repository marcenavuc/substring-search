import time
import pickle
from tests.algorithm_test import ALGORITHMS, TestAlgorithms
import matplotlib.pyplot as plt
import argparse


def delta_time(func, *args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    return end - start


class Benchmark:

    def __init__(self, n_times=100):
        self.tests = TestAlgorithms().TESTS
        self.n_times = n_times

        self.test_time = {}
        for test in self.tests:
            self.test_time[test.name] = {}
            for algorithm in ALGORITHMS:
                self.test_time[test.name][algorithm.name] = []

    def run(self):
        for algorithm in ALGORITHMS:
            for test in self.tests:
                for i in range(self.n_times):
                    self.test_time[test.name][algorithm.name].append(
                        delta_time(algorithm.search, test.substring, test.text)
                    )
        self.save_results()

    def save_results(self):
        with open('results.pickle', 'wb') as file:
            pickle.dump(self.test_time, file)

    def report(self):
        with open('results.pickle', 'rb') as file:
            data = pickle.load(file)

        exp = 1e7
        figure, axises = plt.subplots(len(data), figsize=(15, 30))
        for i, test in enumerate(data):
            for alg in data[test]:
                x_arr = range(len(data[test][alg]))
                y_arr = list(map(lambda x: x * exp, data[test][alg]))

                axises[i].scatter(x_arr, y_arr,label=alg)
                axises[i].set_title(test)
                axises[i].set_xlabel('runs')
                axises[i].set_ylabel(f'time powed {exp}')
                axises[i].legend()
        figure.savefig('report.png', format='png')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple benchmark for '
                                                 'substring searching '
                                                 'algorithms')
    parser.add_argument('N', metavar='N_times', type=int, help='an integer of '
                                                               'times to run '
                                                               'tests')
    parser.add_argument('--report', dest='make_report', action='store_const',
                        const=True, default=False, help='makes report of tests'
                                                       'in report.png')
    args = parser.parse_args()
    benchmark = Benchmark(args.N)
    benchmark.run()
    if args.make_report:
        benchmark.report()
