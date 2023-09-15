#!/usr/bin/python3
def uppercase(str):
    # a function that prints a string in uppercase followed by a new line.
    for c in str:
        asci = ord(c)
        if 97 <= asci <= 122:
            asci -= 32
        print("{}".format(chr(asci)), end='')
    print()
