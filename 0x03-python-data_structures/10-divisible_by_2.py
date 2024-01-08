#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_new = []

    for intg in my_list:
        if intg % 2 == 0:
            my_new.append(True)
        else:
            my_new.append(False)
    return my_new
