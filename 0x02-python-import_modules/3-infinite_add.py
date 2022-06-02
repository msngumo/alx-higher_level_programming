#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print(sum([int(x) for x in argv[1:]]))
