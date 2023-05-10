#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if 'a' <= ord(c) <= 'z':
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("".format())
