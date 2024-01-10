#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    my_matrx = []

    for row in matrix:
        my_row = []
        for i, line in enumerate(row):
            my_row.append(line ** 2)
        my_matrx.append(my_row)

    return my_matrx
