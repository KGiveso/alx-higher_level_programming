#!/usr/bin/python3
def multiple_returns(sentence):
  """Returns a tuple with the length of a string and its first character.

  Args:
    sentence: The string.

  Returns:
    A tuple with the following elements:
      * The length of the string.
      * The first character of the string.

  Raises:
    ValueError: If the sentence is empty.
  """

  # Check if the sentence is empty
  if not sentence:
    raise ValueError("Sentence is empty")

  # Get the length of the sentence
  length = len(sentence)

  # Get the first character of the sentence
  first = sentence[0]

  # Return the tuple
  return (length, first)
