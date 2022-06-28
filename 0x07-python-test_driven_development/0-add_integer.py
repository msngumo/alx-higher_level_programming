#!/usr/bin/python3

"""
Addition
"""

def add_integer(a, b=98):
    """
    Function that adds two integers
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    elif not isinstance(b,int):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        x = int(a)
    if isinstance(b, float):
        y = int(b)

    return(x + y)

