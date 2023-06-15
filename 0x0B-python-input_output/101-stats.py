#!/usr/bin/python3
"""
Sort_dict module.
It contains one function.
"""


import sys

size = 0
count = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
try:
    for line in sys.stdin:
        if count % 10 == 0:
            print("File size: {}".format(size))
            for key, value in sorted(status_codes.items()):
                if value != 0:
                    print("{}: {}".format(key, value))
        for key in status_codes.keys():
            if str(key) in line:
                status_codes[key] = status_codes[key] + 1
        size = line.rsplit(' ', 1)[1]
        size += int(size)
        count += 1
except KeyboardInterrupt:
    print("File size: {}".format(size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))

