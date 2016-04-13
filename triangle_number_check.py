from numbers import Integral
from math import sqrt

def is_triangle_number(number):
    if not isinstance(number, Integral):
        return False
    return sqrt(1 + 8 * number).is_integer()
