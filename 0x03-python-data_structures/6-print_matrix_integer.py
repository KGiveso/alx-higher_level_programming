#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers
    ...

    Parameters
    ----------
    matrix : list (of lists)
        The list to print

    Return:
        None
    """

    for p in range(len(matrix)):
        for a in range(len(matrix[p])):
            print("{:d}".format(matrix[p][a]), end="")
            if a != (len(matrix[p]) - 1):
                print(" ", end="")
        print("")
