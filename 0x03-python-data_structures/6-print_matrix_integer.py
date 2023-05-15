#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
  """Prints a matrix of integers."""
  # Check if matrix is empty
  if not matrix:
    return

  # Iterate over the rows of the matrix
  for row in matrix:
    # Iterate over the columns of the row
    for col in row:
      # Print the column
      print(str.format("{0}", col), end=" ")
    print()
