#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(number):
  """
  Prints the last digit of a number.

  Args:
    number: The number to print the last digit of.

  Returns:
    The last digit of the number.
  """

  print(abs(number) % 10, end="")
  return (abs(number) % 10)


if __name__ == "__main__":
  number = 123
  print_last_digit(number)
