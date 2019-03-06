"""
@author: Tanmay Bhoir

Python script to classify triangles and test cases for checking if the function works properly and doesn't throw any errors. 

"""

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

