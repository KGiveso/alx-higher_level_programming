#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """returns: True - if the object is exactly an instance
    of the specific class, else: False"""

    return type(obj) is a_class
