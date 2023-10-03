#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = list(argv)
    n = len(args)
    add_sum = 0
    for i in range(1, n):
        add_sum += int(args[i])
    print(add_sum)
