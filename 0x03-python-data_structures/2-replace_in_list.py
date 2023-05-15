#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
  """
  Replaces an element of a list at a specific position.

  Args:
    my_list: The list to be modified.
    idx: The index of the element to be replaced.
    element: The new element to be inserted.

  Returns:
    The modified list.
  """

  if idx < 0:
    return my_list

  if idx >= len(my_list):
    return my_list

  for i in range(len(my_list)):
    if i == idx:
      my_list[i] = element
      break

  return my_list
