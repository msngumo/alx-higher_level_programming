#!/usr/bin/python3

"class that defines a square"


class Square:

    """private instance attribute size
    public instance attribute area"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        "getter method: gets value of size"

        return self.__size

    @size.setter
    def size(self, value):
        """
        setter method: sets size to value
        Raise TypeError if size is not an integer
        Raise ValueError if size is < 0
        """

        self.__size = value
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        self.area = self.__size * self.__size
        return self.area
