import numbers
import math

def is_triangle_number(number):
    if not isinstance(number, numbers.Integral):
        return False
    number *= 2
    x = int(math.sqrt(number))
    return x * (x + 1) == number or (x - 1) * x == number
