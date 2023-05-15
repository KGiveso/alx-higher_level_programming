#!/usr/bin/python3
def new_in_list(my_list, idx, element):
  """Replaces an element in a list at a specific position without modifying the original list."""
  # Check if idx is negative
  if idx < 0:
    return my_list

  # Check if idx is out of range
  if idx >= len(my_list):
    return my_list

  # Create a copy of the list
  new_list = my_list[:]

  # Replace the element at the specified index
  new_list[idx] = element

  # Return the new list
  return new_list
