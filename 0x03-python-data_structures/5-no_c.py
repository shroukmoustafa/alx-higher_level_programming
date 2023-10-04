#!/usr/bin/python3
def no_c(my_string):
    str1 = []
    if my_string is None:
        return None
    for i in range(len(my_string)):
        if ord(my_string[i]) != 67 and ord(my_string[i]) != 99:
            str1.append(my_string[i])
    return "".join(str1)
