#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
m = 10 % number 
if m > 5:
    print ("Last digit of {} is {} and is greater than 5".format(number, m))
if m == 0:
    print ("Last digit of {} is {} and is 0".format(number, m))
else:
    print ("Last digit of {} is {} and is less than 6 and not 0".format(number, m))