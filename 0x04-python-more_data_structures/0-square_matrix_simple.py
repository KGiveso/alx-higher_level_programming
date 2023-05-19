#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix

    Return:
        Same size as matrix
        value: is square of the value of the input
    """
    return ([list(map(lambda x: x * x, row)) for row in matrix])
