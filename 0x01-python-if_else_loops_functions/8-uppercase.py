#!/usr/bin/python3
# 8-uppercase.py


def uppercase(str):
  """
  Converts all lowercase letters in a string to uppercase.

  Args:
    str: The string to convert.

  Returns:
    The string with all lowercase letters converted to uppercase.
  """

  for c in str:
    if ord(c) >= 97 and ord(c) <= 122:
      c = chr(ord(c) - 32)
    print("{}".format(c), end="")
  print("")


if __name__ == "__main__":
  str = "hello world"
  uppercase(str)

