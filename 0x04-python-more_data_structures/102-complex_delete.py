#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = [ky for ky, val in a_dictionary.items() if val == value]
    for ky in keys:
        del a_dictionary[ky]
    return (a_dictionary)
