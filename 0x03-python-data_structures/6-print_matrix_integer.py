#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
  """Prints a matrix of integers.

  Args:
    matrix: A list of lists of integers.

  Raises:
    ValueError: If the matrix is not rectangular.

  """
  if not matrix:
    return

  num_rows = len(matrix)
  num_cols = len(matrix[0])

  for row in range(num_rows):
    for col in range(num_cols):
      print("{0:5d}".format(matrix[row][col]), end=" ")
    print()


