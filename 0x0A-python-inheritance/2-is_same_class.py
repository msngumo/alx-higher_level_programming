#!/usr/bin/python3
"checks if obj is an instance of a class"


def is_same_class(obj, a_class):
    if isinstance(obj, a_class) == type(obj).__name__:
        return True
    else:
        return False
