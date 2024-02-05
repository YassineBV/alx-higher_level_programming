#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):
    """
    A custom list class that extends the built-in list class.
    """
    def print_sorted(self):
        """
        Sorts the list in ascending order and prints it.
        """
        self.sort()
        print(self)
