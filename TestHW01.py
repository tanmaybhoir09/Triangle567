import unittest
from HW01 import classify_triangle

class TestClassifyTriangles(unittest.TestCase):
    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), 'scalene')
        self.assertEqual(classify_triangle(7, 12, 10), 'scalene')

    def test_equilateral(self):
        self.assertEqual(classify_triangle(4, 4, 4), 'equilateral')
        self.assertEqual(classify_triangle(7, 7, 7), 'equilateral')

    def test_right(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'right')

    def test_isosceles(self):
        self.assertEqual(classify_triangle(3, 4, 4), 'isosceles')
        self.assertEqual(classify_triangle(5, 7, 7), 'isosceles')

    def test_invalid(self):
        self.assertEqual(classify_triangle(2, 4, 0), 'Invalid')
        self.assertEqual(classify_triangle(-2, -4, 0), 'Invalid')

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)