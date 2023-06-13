#!/usr/bin/python3
"""My list"""


class MyList(list):
    """class inheritance of list class"""

    def print_sorted(self):
        """Prints the list, but sorted orderly"""

        print(sorted(self))
