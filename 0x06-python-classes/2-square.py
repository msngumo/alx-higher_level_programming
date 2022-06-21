#!/usr/bin/python3

"class that defines a square"


class Square:
    "private instane attribute. Size must be an integer"

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
