#!/usr/bin/python3
"""This script finds peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """This function find highest value in list of unsorted integers"""

    my_list = list_of_integers

    if my_list:
        my_list.sort()
        return my_list[-1]
    else:
        return None
