"""Интрефейс алгоритма"""
from abc import ABC, abstractmethod


class Algorithm(ABC):

    @abstractmethod
    def search(self, substring, text):
        pass

    def findall(self, substring, text):
        return list(self.search(substring, text))

    @property
    def name(self):
        return self.__class__.__name__
