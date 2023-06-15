#!/usr/bin/python3
"""
sorted_dict module.
It contains two function.
"""


import signal
import re
import sys


def sorted_dict(d):
    if d:
        print("\n".join(["{}: {:d}".format(k, d[k])
                         for k in sorted(d.keys())]))


def imp_stdin():
    """reads stdin"""
    size = 0
    count = 0
    codes = {}
    possib = ["200", "301", "400", "401", "403", "404", "405", "500"]
    try:
        for line in sys.stdin:
            line_split = line.split()
            if line_split[-1].isdecimal():
                size += int(line_split[-1])
                if line_split[-2] in possib:
                    codes[line_split[-2]] = codes.get(
                        line_split[-2], 0) + 1
            count += 1
            if count % 10 == 0:
                print("File size: {:d}".format(size))
                sorted_dict(codes)
    except KeyboardInterrupt:
        print("File size: {:d}".format(size))
        sorted_dict(codes)
        raise
    print("File size: {:d}".format(size))
    sorted_dict(codes)


imp_stdin()
