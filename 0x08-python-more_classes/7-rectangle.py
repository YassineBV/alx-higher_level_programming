#!/usr/bin/python3
"""A Class representing a rectangle."""


class Rectangle:
    """
   A Class representing a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with the given width and height.

        Args:
            width: The width of the rectangle. Defaults to 0.
            height: The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = self.print_symbol

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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Get the area of the rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Get the perimeter of the rectangle.
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        print() and str() should print the rectangle with the character #
        """
        ptrn = ""
        if self.__height == 0 or self.__width == 0:
            return ptrn
        for i in range(self.__height - 1):
            ptrn += str(self.print_symbol) * self.__width + "\n"
        ptrn += str(self.print_symbol) * self.__width
        return ptrn

    def __repr__(self):
        """return a string representation of the rectangle
        to be able to recreate a new instance
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
        Print  message when an instance of Rectangle is deleted
        """
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
