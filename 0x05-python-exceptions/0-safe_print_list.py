#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        indx = 0
        while x > 0:
            print("{}".format(my_list[indx]), end="")
            x -= 1
            indx += 1
        print()
        return indx
    except IndexError:
        print()
        return indx
