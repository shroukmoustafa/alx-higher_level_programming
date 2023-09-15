#!/usr/bin/python3
def uppercase(str):
    # a function that prints a string in uppercase followed by a new line.
    asci = []
    for char in str:
        asci.append(ord(char) - 32)
        print("{}".format(chr(*asci), end='')
    print()
