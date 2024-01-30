#!/usr/bin/python3
"""
    Write a function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    Adds two integers, Returns: he addition of a and b.
    Args:
    a (int or float): The first number, b : The second number.
    """

    if isinstance(a, float) or isinstance(b, float):
        a = int(a)
        b = int(b)
    if not isinstance(a, int):
        raise TypeError('a must be an integer')
    if not isinstance(b, int):
        raise TypeError('b must be an integer')
    try:
        return a + b
    except TypeError as test:
        print(test)
