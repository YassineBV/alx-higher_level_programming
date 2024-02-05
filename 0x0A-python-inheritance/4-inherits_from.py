#!/usr/bin/python3
"""
function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified
class ; otherwise False.
 """


def inherits_from(obj, a_class):
    """
    Args:
    - obj: The object to be checked.
    - a_class: The class to compare against.
    """
    if type(obj) is a_class:
        return False
    elif isinstance(obj, a_class):
        return True
    else:
        return False
