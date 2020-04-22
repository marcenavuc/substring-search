from algorithms.Algorithm import Algorithm


class BruteForce(Algorithm):

    def search(self, substring, text):
        for i in range(len(text)):
            if text[i: i + len(substring)] == substring:
                yield i
