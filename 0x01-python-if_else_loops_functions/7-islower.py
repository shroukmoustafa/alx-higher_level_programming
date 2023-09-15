#!/usr/bin/python3
def islower(c):
    asci = ord(c)
    for i in range(97, 123):
        if i == asci:
            return (True)
    return (False)
