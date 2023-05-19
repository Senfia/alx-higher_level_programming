#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return (None)
    if matrix == []:
        return ([])
    matrix_sq = [[i*i for i in h-line] for h-line in matrix]
    return (matrix_sq)
