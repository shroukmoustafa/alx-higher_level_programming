#!/usr/bin/python3
def print_last_digit(number):
    n = abs(number) % 10 
    if number < 0:
        n = -n
    print("{}".format(n), end='')
