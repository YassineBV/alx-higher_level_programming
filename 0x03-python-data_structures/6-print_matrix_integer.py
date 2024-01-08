#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for lent, numbr in enumerate(line):
            print("{:d}".format(numbr), end="")
            if lent != (len(line) - 1):
                print("", end=" ")
        print("$")
