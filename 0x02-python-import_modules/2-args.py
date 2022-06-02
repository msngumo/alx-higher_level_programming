#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    length = len(argv)
    if length == 1:
        print("{} arguments.".format(length - 1))
    elif length == 2:
        print("{} argument:".format(length - 1))
        for x, y in enumerate(argv[1:], start=1):
            print("{}: {}".format(x, y))
    else:
        print("{} arguments:".format(length - 1))
        for x, y in enumerate(argv[1:], start=1):
            print("{}: {}".format(x, y))
