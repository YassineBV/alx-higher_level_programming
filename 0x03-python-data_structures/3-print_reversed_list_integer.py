#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for elim in my_list[len(my_list) - 1::-1]:
        print("{:d}".format(elim))
