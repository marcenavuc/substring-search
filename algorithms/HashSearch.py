from algorithms.Algorithm import Algorithm


class RabinKarpSearch(Algorithm):

    @staticmethod
    def search(substring, text):
        window_start = ord(text[0])
        substring_hash = 0
        text_hash = 0
        degree = 1
        for i in range(len(substring) - 1, -1, -1):
            substring_hash += ord(substring[i]) * degree
            text_hash += ord(text[i]) * degree
            degree *= 2
        degree /= 2
        for i in range(len(text) - len(substring) + 1):
            if text_hash == substring_hash \
                    and text[i: i + len(substring)] == substring:
                yield i
            if i < len(text) - len(substring):
                text_hash = (text_hash - degree * window_start) * 2
                window_start = ord(text[i + 1])
                window_end = ord(text[i + len(substring)])
                text_hash += window_end
