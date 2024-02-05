#!/usr/bin/python3
"""
function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    This function takes an object as a parameter
    and returns a list of its attributes and methods.

    Parameters:
    obj (object): The object for which to retrieve the attributes and methods.
    """
    my_list = []
    for elmnt in dir(obj):
        my_list.append(elmnt)
    return my_list
