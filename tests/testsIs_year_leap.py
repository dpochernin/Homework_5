import unittest

from def_for_test import is_year_leap


class TestsYearLeap(unittest.TestCase):

    def testZeroValue(self):
        with self.assertRaises(ValueError):
            is_year_leap(0)

    def testNoValue(self):
        with self.assertRaises(TypeError):
            is_year_leap()

    def testWrongTypeValue(self):
        with self.assertRaises(TypeError):
            is_year_leap('s')

    def testMinusValue(self):
        res = is_year_leap(-1)
        self.assertFalse(res)

    def testMaxValue(self):
        with self.assertRaises(TypeError):
            is_year_leap(float('inf'))

    def test2000Value(self):
        res = is_year_leap(2000)
        self.assertTrue(res)

    def test1800Value(self):
        res = is_year_leap(1800)
        self.assertFalse(res)
