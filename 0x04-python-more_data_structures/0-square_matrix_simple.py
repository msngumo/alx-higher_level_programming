#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in matrix:
        new = []
        for y in x:
            z = y * y
            new.append(z)
        new_matrix.append(new)

    return new_matrix
