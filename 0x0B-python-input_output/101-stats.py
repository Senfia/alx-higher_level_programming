#!/usr/bin/python3
"""
Sort_dict module.
It contains one function.
"""


import sys
from collections import defaultdict

"""Initialize metrics"""
total_file_size = 0
status_code_counts = defaultdict(int)

try:
    for i, line in enumerate(sys.stdin, 1):
        """ Parse input line"""
        parts = line.strip().split()
        if len(parts) >= 7:
            status_code = parts[5]
            file_size = int(parts[6])

            total_file_size += file_size
            status_code_counts[status_code] += 1

        if i % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for code in sorted(status_code_counts.keys()):
                count = status_code_counts[code]
                print(f"{code}: {count}")
            print()

except KeyboardInterrupt:
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        count = status_code_counts[code]
        print(f"{code}: {count}")

