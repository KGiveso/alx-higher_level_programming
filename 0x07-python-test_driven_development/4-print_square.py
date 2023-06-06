#!/usr/bin/python3
"""Write a function that prints a square with the character"""


def print_square(size):
    """ Args:
            size (int): length of the square
        Raise:
            TypeError if size is not an int
            ValueError if size is less than 0
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for rows in range(size):
        for cols in range(size):
            print("#", end="")
        print("")
