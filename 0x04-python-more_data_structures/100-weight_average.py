#!/usr/bin/python3

def weight_average(my_list=[]):
    """Return the weighted average of all integers in a list of tuples."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    average = 0
    size = 0
    for tuplè in my_list:
        average += (tuplè[0] * tuplè[1])
        size += tuplè[1]
    return (average / size)
