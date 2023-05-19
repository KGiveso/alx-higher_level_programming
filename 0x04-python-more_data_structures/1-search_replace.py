#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replace all occurrences of an element by another in a new list."""
    NewList = my_list[:]
    for i in range(len(NewList)):
        if NewList[i] == search:
            NewList[i] = replace
    return (NewList)
