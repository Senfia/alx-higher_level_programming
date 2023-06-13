#!/usr/bin/python3
"""
This is module my_list

It contains one class.
"""


class MyList(list):
    """
    prints the list, but sorted (ascending sort)

    Assumes all the elements in the list are of type int
    """

    def print_sorted(self):
        """print the list in sorted ascending order"""
        print("[" + ", ".join("{:d}".format(i) for i in sorted(self)) + "]")
