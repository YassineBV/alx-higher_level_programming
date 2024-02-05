#!/usr/bin/python3
"""
function that returns True if the object is an instance of
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False."""


def is_kind_of_class(obj, a_class):
    """
    Args:
    - obj: The object to be checked.
    - a_class: The class to compare against.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
