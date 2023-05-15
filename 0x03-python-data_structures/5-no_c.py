#!/usr/bin/python3
def no_c(str):
    new_str = ""
    for ch in str:
        if (ch != 'c' and ch != 'C'):
            new_str += ch
    return (new_str)
