#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    current_list = my_list.copy()
    if not (idx > len(current_list) - 1 or idx < 0):
        current_list[idx] = element
    return current_list
