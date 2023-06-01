#!/usr/bin/python3
"""Square class that defines a square and checks for errors"""
"""__init__ - initialize a square class

    size - size of square intialize 0
    """

class Square:
    
    def __init__(self, size=0):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
