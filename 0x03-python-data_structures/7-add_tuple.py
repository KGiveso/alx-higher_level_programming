#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Extract the first two integers from each tuple
    a = tuple_a[:2]
    b = tuple_b[:2]

    # If a tuple is smaller than 2, append 0 to make it a 2-element tuple
    if len(a) < 2:
        a += (0,) * (2 - len(a))
    if len(b) < 2:
        b += (0,) * (2 - len(b))

    # Add the corresponding elements from both tuples
    result = (a[0] + b[0], a[1] + b[1])
    return result
