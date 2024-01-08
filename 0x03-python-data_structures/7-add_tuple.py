#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_tup = tuple()
    if len(tuple_a) == 0:
        my_tup = (tuple_b[0] + 0, tuple_b[1] + 0)
    elif len(tuple_b) == 0:
        my_tup = (tuple_a[0] + 0, tuple_a[1]+ 0)
    elif len(tuple_a) == 1:
        my_tup = (tuple_a[0] + tuple_b[0], tuple_b[1] + 0)
    elif len(tuple_b) == 1:
        my_tup = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
    else:
        my_tup = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return my_tup
