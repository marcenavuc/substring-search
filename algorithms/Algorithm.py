"""Интрефейс алгоритма"""
from abc import ABC, abstractstaticmethod
from algorithms.BigIO import BigIO


class Algorithm(ABC):

    @abstractstaticmethod
    def search(substring, text):
        pass

    @classmethod
    def findall(cls, substring, text):
        return list(cls.search(substring, text))

    @classmethod
    def name(cls):
        return cls.__name__

    # @classmethod
    # def big_findall(cls, filename, substring):
    #     try:
    #         result = []
    #         with open(filename) as file:
    #             line = file.readline()
    #             while line:
    #                 if len(line) >= len(substring):
    #                     match = list(cls.search(substring, line))
    #                     match = list(map(lambda s: s + file.tell() - len(line),
    #                                      match))
    #                     result.extend(match)
    #                 line = file.readline()
    #
    #         return result
    #     except Exception as e:
    #         print("Error with file. Try later", e)
    #         return []

    @classmethod
    def big_findall(cls, filename, substring):
        try:
            with BigIO(filename) as bigio:
                return cls.findall(substring, bigio)
        except Exception as e:
            print("Error with file. Try again later", e)
            return []
