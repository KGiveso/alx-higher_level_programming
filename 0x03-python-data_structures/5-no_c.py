#!/usr/bin/python3
def no_c(my_string):
  """
    Removes all characters c and C from a string
    ...

    Parameters
    ----------
    my_string : str
        The string to remove 'Cc' from

    Return:
        The new string
    """

  # Create a new list to store the characters that are not c or C
  new_list = []
  for c in my_string:
    if c not in ['c', 'C']:
      new_list.append(c)

  # Return the new string
  return ''.join(new_list)
