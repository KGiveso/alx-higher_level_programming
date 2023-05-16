#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
  """Prints a matrix of integers.

  Args:
    matrix: A list of lists, where each inner list contains an integer.

  Raises:
    ValueError: If the matrix is not a list of lists.

  """
  if not isinstance(matrix, list):
    raise ValueError("matrix must be a list of lists")

  for row in matrix:
    for value in row:
      print(str.format("{}", value), end=" ")
    print()

