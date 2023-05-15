#!/usr/bin/python3
def max_integer(my_list=[]):
  """Finds the biggest integer of a list.

  Args:
    my_list: The list of integers.

  Returns:
    The biggest integer of the list.

  Raises:
    ValueError: If the list is empty.
  """

  # Check if the list is empty
  if not my_list:
    raise ValueError("List is empty")

  # Initialize the biggest integer
  biggest_integer = my_list[0]

  # Iterate over the list
  for integer in my_list:
    # If the current integer is bigger than the biggest integer, update the biggest integer
    if integer > biggest_integer:
      biggest_integer = integer

  # Return the biggest integer
  return biggest_integer
