#!/usr/bin/python3
"""Write class squar that access and update private attribute"""


class Square:
    """__init__method that initialize a square class
    Args:
        size: size of square
    """
    def __init__(self, size=0):
        self._size = size

    @property
    def size(self):
        """find the instance attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        """Record value to size and checks for errors"""

        if type(value) != int:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """finds the area of square
        Return:
            area of the square
        """

        return self.__size * self.__size
