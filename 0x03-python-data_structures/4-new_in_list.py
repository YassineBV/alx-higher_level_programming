#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_new = my_list[:]
    if idx < 0:
        return my_new
    elif idx > len(my_list) - 1:
        return my_new
    else:
        my_new[idx] = element
        return my_new
