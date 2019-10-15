import unittest

from def_for_test import triangle_possible


class TestsTrianglePossible(unittest.TestCase):

    def testMaxValue(self):
        res = triangle_possible(float('inf'), float('inf'), float('inf'))
        self.assertTrue(res)

    def testMinusValue(self):
        with self.assertRaises(ValueError):
            triangle_possible(-1, -1, -1)

    def testZeroValue(self):
        with self.assertRaises(ValueError):
            triangle_possible(0, 0, 0)

    def testWrongType(self):
        with self.assertRaises(TypeError):
            triangle_possible('a', 'b', 'c')

    def testNormalTriangle(self):
        res = triangle_possible(1, 1, 1)
        self.assertTrue(res)

    def testNotPossibleTriangle(self):
        res = triangle_possible(1.5, 1.5, 3)
        self.assertFalse(res)
