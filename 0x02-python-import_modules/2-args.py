#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = list(argv)
    if len(argv) == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(len(argv) - 1))
        for i , arg in enumerate(args):
            if i > 0:
                print("{}: {}".format(i, arg))
