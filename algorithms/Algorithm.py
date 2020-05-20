"""Интрефейс алгоритма"""
from abc import ABC, abstractmethod
from algorithms.BigIO import BigIO


class Algorithm(ABC):

    @staticmethod
    @abstractmethod
    def search(substring, text):
        pass

    @classmethod
    def findall(cls, substring, text):
        return list(cls.search(substring, text))

    @classmethod
    def name(cls):
        return cls.__name__

    @classmethod
    def big_findall(cls, io_object, substring):
        try:
            with BigIO(io_object) as bigio:
                return cls.findall(substring, bigio)
        except Exception as e:
            print("Error with file. Please, Try again later", e)
            return []
