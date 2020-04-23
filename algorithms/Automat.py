from algorithms.Algorithm import Algorithm


class Automat(Algorithm):

    @staticmethod
    def search(substring, text):
        # Определяем алфавит
        alphabet = {}
        transition = [{} for i in range(len(substring) + 1)]
        for letter in substring:
            transition[0][letter] = 0
            alphabet[letter] = 0
        # присваиваем значения ячейкам матрицы переходов
        for i in range(len(substring)):
            prev = transition[i][substring[i]]  # значение текущего состояния
            transition[i][substring[i]] = i + 1
            for letter in alphabet.keys():
                transition[i + 1][letter] = transition[prev][letter]

        current_state = 0
        end_state = len(substring)
        for i in range(len(text)):
            if text[i] in alphabet.keys():  # если такой символ есть в алфавите
                current_state = transition[current_state][text[i]]
            else:
                current_state = 0

            if current_state == end_state:
                yield i - len(substring) + 1
