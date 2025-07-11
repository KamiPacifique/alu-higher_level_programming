#!/usr/bin/python3
"""Defines a Rectangle class inheriting from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Both width and height must be validated as positive integers.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @property
    def height(self):
        """Height getter."""
        return self.__height
