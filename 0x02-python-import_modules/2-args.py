#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = []
    x = sys.argv
    if len(x) == 1:
        print("0 arguments.")
    elif len(x) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(x) - 1))
    for i, ar in enumerate(x):
        if i > 0:
            print("{}: {}".format(i, ar))
