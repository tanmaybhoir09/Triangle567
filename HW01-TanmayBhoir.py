"""
@author: Tanmay Bhoir

Python script to classify triangles and test cases for checking
if the function works properly and doesn't throw any errors. 

"""
import unittest

def classify_triangle(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return 'Invalid'
    if a is False or b is False or c is False:
        return None
    if a is True or b is True or c is True:
        return None
    if a < 0 or b < 0 or c < 0:
        return None

    round_a = round(a, 2)
    round_b = round(b, 2)
    round_c = round(c, 2)

    if round((a + b) / 2, 2) == round_a:
        return "equilateral"
    if round(a ** 2 + b ** 2, 2) == round(c ** 2, 2):
        return "right"
    if round_a == round_b or round_b == round_c or round_c == round_a:
        return "isosceles"
    return "scalene"


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