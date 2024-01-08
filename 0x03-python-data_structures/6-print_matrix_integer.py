#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for numbr in range(len(line)):
            if numbr == (len(line) - 1):
                print("{:d}".format(line[numbr]), end="")
            else:
                print("{:d}".format(line[numbr]), end=" ")
        print()
