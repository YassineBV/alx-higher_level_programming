#!/usr/bin/python3
from sys import argv
argvlent = len(argv)
if __name__ == "__main__":
    if argvlent == 1:
        print("0 arguments.")
    elif argvlent == 2:
        print("1 argument.")
        print("{}: {}".format(1, argv[1]))
    elif len(argv) > 2:
        print("{} arguments.".format(len(argv) - 1))
        for i in range(1, argvlent):
            print("{}: {}".format(i, argv[i]))
