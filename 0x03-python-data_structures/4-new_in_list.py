#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list is None:
        return None
    if idx < 0:
        return my_list
    if idx > (len(my_list) - 1):
        return my_list
    b = my_list
    b[idx] = element
    return b
