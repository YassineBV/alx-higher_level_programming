#!/usr/bin/python3
"""
function that Checks if the given object is an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if the given object is an instance of the specified class.

    Args:
    - obj: The object to be checked.
    - a_class: The class to compare against.

    Returns:
    - True if the object is an instance of the specified class
    False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
