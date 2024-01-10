#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for numbr in my_list:
        if numbr == search:
            new_list.append(replace)
            continue
        new_list.append(numbr)
    return new_list
