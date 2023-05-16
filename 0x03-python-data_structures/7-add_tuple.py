#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
  """Adds 2 tuples.

  Args:
    tuple_a: The first tuple.
    tuple_b: The second tuple.

  Returns:
    A tuple with 2 integers:
      The first element should be the addition of the first element of each argument
      The second element should be the addition of the second element of each argument

  Raises:
    ValueError: If either tuple is empty.
  """
  # Check if either tuple is empty
  if not tuple_a:
    a1 = 0
  else:
    a1 = tuple_a[0]

  if not tuple_b:
    a2 = 0
  else:
    a2 = tuple_b[0]

  # Add the first two elements of each tuple
  c1 = a1 + b1
  c2 = a2 + b2

  # Return the resulting tuple
  return (c1, c2)


