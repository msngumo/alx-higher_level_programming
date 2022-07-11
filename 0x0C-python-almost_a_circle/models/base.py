#!/usr/bin/python3


class Base:
    __nb_objects = 0
    "private class attribute"

    def __init__(self, id=None):
        "class constructor"

        if id is None:
            Base.__nb_objects += 1
            id = Base.__nb_objects
        self.id = id
