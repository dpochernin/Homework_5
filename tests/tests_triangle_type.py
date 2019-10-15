import unittest

from def_for_test import triangle_type

class TestsTriangleType(unittest.TestCase):

    def testMaxValue(self):
        res = triangle_type(float('inf'), float('inf'), float('inf'))
        self.assertEqual(res, 'Equilateral triangle')

    def testEquilateralTriangle(self):
        res = triangle_type(1, 1, 1)
        self.assertEqual(res, 'Equilateral triangle')

    def testIsoscelesTriangle(self):
        res = triangle_type(2, 2, 3)
        self.assertEqual(res, 'Isosceles triangle')

    def testIsoscelesTriangle(self):
        res = triangle_type(1, 2, 3)
        self.assertEqual(res, 'Versatile triangle')

    def testMinusValue(self):
        res = triangle_type(-1, -1, -1)
        self.assertEqual(res, 'Not a triangle')

    def testZeroValue(self):
        res = triangle_type(0, 0, 0)
        self.assertEqual(res, 'Not a triangle')

    def testWrongType(self):
        res = triangle_type('a', 'b', 'c')
        self.assertEqual(res, 'Not a triangle')
