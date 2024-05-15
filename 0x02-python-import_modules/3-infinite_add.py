#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = []
    x = sys.argv
    s = 0
    for i, n in enumerate(x):
        if i > 0:
            s += int(n)
    print(f"{s}")
