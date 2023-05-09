#!/usr/bin/python3
def uppercase(string):
    upper_case = [chr(ord(char) - 32) if ord(char) >= ord('a') and ord(char) <= ord('z') else char for char in string]
    print("".join(upper_case))

