#!/usr/bin/python3
"""
matrix_divided
"""


def matrix_divided(matrix, div):
    """
    divides a matrix using div
    """

    err_1 = "matrix must be a matrix (list of lists) of integers/floats"

    if not any(isinstance(row, list) for row in matrix):
        raise TypeError(err_1)
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_1)
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(err_1)

    return [[round((y / div), 2)for y in x]for x in matrix]
