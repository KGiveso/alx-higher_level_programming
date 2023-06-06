#!/usr/bin/python3
"""Write a function that prints a text with 2 new lines after each char ., ? and :
"""


def max_integer(list=[]):
    """Strings: list of integer
        Return:
            If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
