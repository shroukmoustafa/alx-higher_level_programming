#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    for i in range(len(my_string)):
        if my_string[i] == c or my_string[i] == C:
            del my_string[i]
    return my_string
