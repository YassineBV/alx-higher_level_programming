#!/usr/bin/python3
def lookup(obj):
    my_list = []
    for elmnt in dir(obj):
        my_list.append(elmnt)
    return my_list
