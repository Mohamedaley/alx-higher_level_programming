#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        for item in row:
            new[row][item] = (matrix[row][item] ** 2)
    return new
