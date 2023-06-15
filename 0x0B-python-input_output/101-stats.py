#!/usr/bin/python3
"""
Sort_dict module.
It contains one function.
"""

import sys

def sort_dict(dic):
    """
    reads stdin line by line and computes metrics
    """
    for i in sorted(dic.keys()):
        print("{}: {:d}".format(i, dic[i]))
try:
    size = 0
    count = 0
    status_code = {}
    for line in sys.stdin:
        size += int(line.split()[-1])
        status_code[line.split()[-2]] = status_code.get(line.split()[-2], 0) + 1
        count += 1
        if count % 10 == 0:
            print("File size: {:d}".format(size))
            sort_dict(status_code)
except KeyboardInterrupt as e:
        print("File size: {:d}".format(size))
        sort_dict(status_code)
        print(e)
