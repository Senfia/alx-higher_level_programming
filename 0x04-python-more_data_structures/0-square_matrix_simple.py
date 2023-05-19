#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_sq = []
    if matrix:
        for x in matrix:
            coln = []
            for y in x:
                coln.append(y * y)
            matrix_sq.append(coln)
    return matrix_sq
