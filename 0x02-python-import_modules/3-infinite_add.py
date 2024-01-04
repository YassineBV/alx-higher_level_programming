#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0
    for toIntj in argv[1:]:
        sum += int(toIntj)
    print("{}".format(sum))
