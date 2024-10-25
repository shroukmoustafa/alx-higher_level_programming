#!/usr/bin/python3
for a in range(ord('a'), ord('z') + 1):
    if (a == 101) or (a == 113):
        continue
    print("{}".format(chr(a)), end='')
