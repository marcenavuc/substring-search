import unittest
import io
from algorithms.BigIO import BigIO


class TestBigIO(unittest.TestCase):

    def setUp(self):
        self.ABS_TEXT = io.StringIO("abcde")
        self.bigio = BigIO(self.ABS_TEXT)

    def test_indexing(self):
        self.assertEqual(self.bigio[0], 'a')
        self.assertEqual(self.bigio[4], 'e')
        self.assertEqual(self.bigio[1], 'b')
        self.assertEqual(self.bigio[3], 'd')
        self.assertEqual(self.bigio[2], 'c')

    def test_length(self):
        self.assertEqual(len(self.bigio), 5)

    def test_slicing(self):
        self.assertEqual(self.bigio[0: 2], 'ab')
        self.assertEqual(self.bigio[0: 3], 'abc')
        self.assertEqual(self.bigio[1: 3], 'bc')
        self.assertEqual(self.bigio[1: 4], 'bcd')


if __name__ == '__main__':
    unittest.main()
