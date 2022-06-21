#!/usr/bin/python3

"class that defines a square"


class Square:

    """private instance attribute size
    public instance attribute area"""

    def __init__(self, size=0):
        self.__size = size

        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= o")

    def area(self):
        self.area = self.__size * self.__size
        return self.area
