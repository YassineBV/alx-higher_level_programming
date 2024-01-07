#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for numbr in line:
            print("{:d}".format(numbr), end=" ")
        print()
