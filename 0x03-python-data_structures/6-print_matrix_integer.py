#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for b in row:
            print("{:d}".format(b), end="")
            if row.index(b) < len(row) - 1:
                print(" ", end="")
        print()
