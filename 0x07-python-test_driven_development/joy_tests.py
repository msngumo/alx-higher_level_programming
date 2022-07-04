#!/usr/bin/python3

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

"""main = [[round((y / 3), 2) for y in x] for x in matrix]"""

if any(isinstance(x, list) for x in matrix):
    print(True)

else:
    print(False)

