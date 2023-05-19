#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        val = list(a_dictionary.values())
        key_a = list(a_dictionary.keys())
        return key_a[val.index(max(val))]
