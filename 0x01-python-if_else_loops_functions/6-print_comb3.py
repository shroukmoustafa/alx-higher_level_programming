#!/usr/bin/python3
for i in range(0,8):
     for j in range(0,10):
        if j > i:
            print("{:02d}".format(i * 10 + j), end='')
            print(', ', end='')
print("{:02d}".format((i + 1) * 10 + j))
