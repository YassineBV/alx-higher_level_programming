#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_dictionary = sorted(a_dictionary.keys())
    for key in my_dictionary:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
