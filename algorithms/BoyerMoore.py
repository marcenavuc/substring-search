from algorithms.Algorithm import Algorithm

ANY_LETTER = '*'


def same(x, y):
    for p in range(len(x)):
        if x[p] != ANY_LETTER and y[p] != ANY_LETTER and x[p] != y[p]:
            return False
    return True


class BoyerMooreSearch(Algorithm):

    @staticmethod
    def create_shift_table(substring):
        sub = ANY_LETTER * len(substring) + substring
        shift_arr = [len(substring)] * len(substring)
        shift_arr[0] = 1
        for i in range(len(substring)):
            for j in range(len(substring)):
                # Запоминаем кол-во символов необходимых для сдвига на
                # конкретном символе
                left_edge = len(substring) - i
                window = len(sub) - j
                if same(substring[left_edge:], sub[window - i: window]) \
                        and substring[left_edge - 1] != sub[window - i - 1]:
                    break
            shift_arr[i] = min(len(substring), j)

        return shift_arr

    @staticmethod
    def search(substring, text):
        stop_table = {substring[i]: i for i in range(len(substring))}
        shift_table = BoyerMooreSearch.create_shift_table(substring)

        # Ищем в тексте шаблон
        i = 0
        while i < len(text) - len(substring) + 1:
            sub_text = text[i: i + len(substring)]
            if sub_text == substring:
                yield i
                i += 1
                continue
            # Если подстроки не совпали
            # Находим индекс на котором подстроки не совпали
            for j in range(len(substring) - 1, -1, -1):
                if sub_text[j] != substring[j]:
                    break

            if substring[j] in stop_table:
                step_stop = j - stop_table[substring[j]]
            else:
                stop_table = j + 1

            step_shift = shift_table[len(substring) - j - 1]
            if max(step_stop, step_shift) > 1:
                i += max(step_stop, step_shift)
            i += 1
