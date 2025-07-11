#!/usr/bin/python3
"""Defines a Rectangle class with instance counting."""


class Rectangle:
    """Rectangle class with width, height, and instance tracking."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize rectangle and increment instance count."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter or 0 if width or height is 0."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return rectangle as '#' string or empty if 0 dimension."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Return string to recreate instance."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print message on deletion and decrement instance count."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
