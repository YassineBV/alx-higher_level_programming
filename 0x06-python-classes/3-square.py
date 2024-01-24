#!/usr/bin/python3
"""A class representing a square."""


class Square:
    """
    Attributes:
    - __size (int): The size of the square.

    Methods:
    - __init__(self, size=0):
        Initializes a Square object with the specified size.
    - area(self):
        Calculates and returns the area of the square.
        Returns:
            The area of the square, which is the square of the size.
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size * self.__size
