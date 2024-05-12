#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = []
    x = sys.args
    s = 0
    for i in x:
        s += i
    print(f"{s}")
