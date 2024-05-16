#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > (len(my_list) - 1):
        return None
    element = my_list[idx]
    print("Element at index {:d} is {:d}".format(idx, element))
