#!/usr/bin/python3
"""Calculate a MagicClas matching exactly a bytecode """

import math


class MagicClas:
    """presents a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.
        String:
            radius: The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be an integer")
        self.__radius = radius

    def area(self):
        """Return : area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return : circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
