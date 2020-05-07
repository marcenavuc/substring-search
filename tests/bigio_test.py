import unittest
from algorithms.BigIO import BigIO


class TestBigIO(unittest.TestCase):

    def test_indexing(self):
        with BigIO('abc.txt') as bigio:
            self.assertEqual(bigio[0], 'a')
            self.assertEqual(bigio[4], 'e')
            self.assertEqual(bigio[1], 'b')
            self.assertEqual(bigio[3], 'd')
            self.assertEqual(bigio[2], 'c')

    def test_length(self):
        with BigIO('abc.txt') as bigio:
            self.assertEqual(len(bigio), 5)

    def test_slicing(self):
        with BigIO('abc.txt') as bigio:
            self.assertEqual(bigio[0: 2], 'ab')
            self.assertEqual(bigio[0: 3], 'abc')
            self.assertEqual(bigio[1: 3], 'bc')
            self.assertEqual(bigio[1: 4], 'bcd')


if __name__ == '__main__':
    unittest.main()
