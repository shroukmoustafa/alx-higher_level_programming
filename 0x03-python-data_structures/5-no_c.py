#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        newstring = "".join(c for c in my_string if (c != 'c' and c != 'C'))
        return newstring
    return my_string
