#!/usr/bin/python3
def print_reversed_list_integer(mylist=[]):
    if (mylist is None):
        return (None)
    for n in reversed(mylist):
        print("{:d}".format(n))
