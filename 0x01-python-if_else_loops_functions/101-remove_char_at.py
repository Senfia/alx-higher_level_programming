#!/usr/bin/python3
def remove_char_at(str, num):
    if (num >= 0):
        str = str[:num] + str[num + 1:]
    return (str)
