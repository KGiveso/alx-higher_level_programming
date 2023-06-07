#!/usr/bin/python3
"""Low memory cost"""


class LockedClass:
    """class with only one attribute"""
    __slots__ = ("first_name",)
