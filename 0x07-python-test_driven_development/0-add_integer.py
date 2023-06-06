#!/usr/bin/python3
"""Write funtion that add 2 integer"""


def add_integer(a, b=98):
    """Returns the addition of a and b
        Float args are typecasted to ints
        TypeError: if a or b is not int or float
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
