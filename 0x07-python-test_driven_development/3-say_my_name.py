#!/usr/bin/python3
"""Write function that prints string()"""


def say_my_name(first_name, last_name=""):
    """Print my name is <first_name> <last_name>

    Strings:
        first_name (str): first name
        last_name (str): last name
    Raises:
        raise TypeError if first_name and last_name are not strings
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
print("My name is {first_name} {last_name}")
