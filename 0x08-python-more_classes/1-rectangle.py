#!/usr/bin/python3
""" class Rectangle that defines a rectangle"""


class Rectangle:
    """
    A class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with the given width and height.

        Args:
            width: The width of the rectangle. Defaults to 0.
            height: The height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Get the width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Get the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.
        """
        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        self.__height = value
    def __dict__(self):
        """
        Return a modified dictionary representation of the rectangle.
        """
        return dict(reversed(self.__dict__.items()))