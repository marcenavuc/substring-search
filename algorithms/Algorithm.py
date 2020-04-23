"""Интрефейс алгоритма"""
from abc import ABC, abstractstaticmethod


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
