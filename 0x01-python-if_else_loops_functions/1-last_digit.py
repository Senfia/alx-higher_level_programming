#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number < 0):
    mydigit = (number * -1 % 10) * -1
else:
    mydigit = number % 10
if (mydigit > 5):
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, mydigit))
elif (mydigit < 6 and mydigit != 0):
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, mydigit))
else:
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, mydigit))
