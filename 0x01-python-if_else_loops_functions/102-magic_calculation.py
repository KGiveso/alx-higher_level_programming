def magic_calculation(a, b, c):
  """
  Does a magic calculation with three numbers.

  Args:
    a: The first number.
    b: The second number.
    c: The third number.

  Returns:
    The result of the magic calculation.
  """

  if a < b:
    return c
  elif c > b:
    return a + b
  else:
    return a * b - c

