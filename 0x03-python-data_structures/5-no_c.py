#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    for i in range(len(my_string)):
        if ord(my_string[i]) == 67 or ord(my_string[i]) == 99:
            del my_string[i]
    return my_string
