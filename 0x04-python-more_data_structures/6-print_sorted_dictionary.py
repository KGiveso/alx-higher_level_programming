#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Print a dictionary by ordered keys."""
    [print("{}: {}".format(x, a_dictionary[x])) for x in sorted(a_dictionary)]
