#!/usr/bin/python3
"""
pascal_triangle module.
"""


def pascal_triangle(n):
    """
    Returns an empty list if n <= 0
    """
    if n <= 0:
        return []
    
    rows = [[1 for j in range(i + 1)] for i in range(n)]
    n_val = 0
    
    while n_val < n:
        i = 0
        while i < n_val - 1:
            rows[n_val][i + 1] = sum(rows[n_val - 1][i:i + 2])
            i += 1
        n_val += 1

    return rows
