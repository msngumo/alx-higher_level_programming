#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    """

    if isinstance(matrix, list):
        for x, y in matrix:
            if type(x) or type(y) not in [list, int]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(x) != len(y):
                raise TypeError("Each row of the matrix must have the same size")
            if type(div) not in [int, float]:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")

