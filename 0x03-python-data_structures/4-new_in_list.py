#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx >= 0 and idx < (len(my_list)):
        my_list1 = my_list
        my_list1[idx] = element
        return (my_list1)
    else:
        return (my_list)
