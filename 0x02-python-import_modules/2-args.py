#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = list(argv)
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:")
        print("1: {}".format(args[1]))
    else:
        print("{} arguments:".format(len(argv) - 1))
        for i, arg in enumerate(args):
            if i > 0:
                print("{}: {}".format(i, arg))
