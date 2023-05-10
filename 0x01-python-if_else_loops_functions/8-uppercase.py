#!/usr/bin/python3
def uppercase(str):
    for stri in str:
        if ord(stri) >= ord('a') and ord(stri) <= ord('z'):
            stri = chr(ord(i) - 32)
        print("{:s}".format(stri), end="")
    print()
