#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
  """Prints all integers of a list, in reverse order."""
  for i in range(len(my_list) - 1, -1, -1):
    print(str.format("{0}", my_list[i]))
