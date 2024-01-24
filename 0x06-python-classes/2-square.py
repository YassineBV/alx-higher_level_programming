#!/usr/bin/python3
class Square:
    """Square that defines a square by: (based on 1-square.py)

    Private instance attribute: size
    Instantiation with optional size: def __init__(self, size=0)
    """
    def __init__(self, size=0):
        try:
            self._Square__size = size
            if size < 0:
                raise ValueError("size must be >= 0")

        except TypeError:
            print("size must be an integer")
