#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_prt = 0
    for elmnt in range(x):
        if not isinstance(my_list[elmnt], int):
            continue
        print("{:d}".format(my_list[elmnt]), end="")
        nb_prt += 1
    print()
    try:
        return nb_prt
    except TypeError:
        return None
