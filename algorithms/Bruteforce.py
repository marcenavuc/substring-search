from algorithms.Algorithm import Algorithm


class BruteForce(Algorithm):

    @staticmethod
    def search(substring, text):
        for i in range(len(text)):
            if text[i: i + len(substring)] == substring:
                yield i
