#!/usr/bin/python3
"Defines a class"


class Rectangle:
    "Defines a rectangle"
    def __init__(self, width=0, height=0):
        "instantiates width and height"
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        "defining area"
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        new_str = ""
        if self.__width == 0 or self.__height == 0:
            return new_str
        else:
            for x in range(self.__height):
                for y in range(self.__width):
                    new_str += "#"
                if x != self.__height - 1:
                    new_str += "\n"
            return new_str
    def __repr__(self):
        return '{self.__class__.__name__}({self.height}, {self.width})'.format(self=self)








