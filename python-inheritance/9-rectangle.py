#!/usr/bin/python3
"""Module for Rectangle class that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculate area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return string representation of the rectangle."""
        return f"[Rectangle] {self.__width}/{self.__height}"
