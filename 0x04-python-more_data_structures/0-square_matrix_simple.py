#!/usr/bin/python3
def square(x):
    return (x * x)


def square_matrix_simple(matrix=[]):
    newmatrix = []
    for row in matrix:
        row2 = list(map(square, row))
        newmatrix.append(row2)
    return newmatrix
