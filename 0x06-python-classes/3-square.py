#!/usr/bin/python3
"""Write class square defined that calculates the area of a square"""


class Square:
    """__init__method that initialize a square class
    Arguments:
        size: size of square
    """

    def __init__(self, size=0):
        self.__size = size
        if type(size) != int
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """find the total area of the square

        Return:
             area of the square
        """

        return self.__size * self.__size
