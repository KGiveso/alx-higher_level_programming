
#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
  """
  Deletes the item at a specific position in a list.

  Args:
    my_list: The list to delete from.
    idx: The index of the item to delete.

  Returns:
    The list with the item deleted.
  """

  if idx < 0 or idx >= len(my_list):
    return my_list

  # Get the item to delete.
  item_to_delete = my_list[idx]

  # Shift all the items after the deleted item one position to the left.
  for i in range(idx + 1, len(my_list)):
    my_list[i - 1] = my_list[i]

  # Remove the last item in the list.
  my_list.pop()

  return my_list
