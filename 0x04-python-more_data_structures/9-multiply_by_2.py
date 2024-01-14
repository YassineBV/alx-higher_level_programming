#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key in a_dictionary:
        valu = a_dictionary[key]
        new_dictionary[key] = valu * 2
    return new_dictionary
