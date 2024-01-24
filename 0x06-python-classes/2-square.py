#!/usr/bin/python3
"""Square that defines a square"""


class Square:
    """
    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0)
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
