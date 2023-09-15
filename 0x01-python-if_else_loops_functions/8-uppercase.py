#!/usr/bin/python3
def uppercase(str):
    # a function that prints a string in uppercase followed by a new line.
    new_str = ""
    for c in str:
        asci = ord(c)
        if 97 <= asci <= 122:
            asci -= 32
        new_str += chr(asci)
    print("{}".format(new_str))
