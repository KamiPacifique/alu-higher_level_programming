#!/usr/bin/python3
"""
Module: write_file
This module provide a function to write a string to a UTF-8 encoded text file
"""


def write_file(filename="", text=""):
    """
    Write a string to  text file and returns the number of character written.

    Args:
        filename (str): The name or path of the file to write to.
        text (str): The string to write to the file.

    Returns:
        int: The number of characters written to the file.

    Notes:
        - Uses the 'with' statement for proper file handling.
        - Creates the file if it doesn't exist.
        - Overwrites the file if it already exists.
        - Assumes file permissions are adequate and does not handle exception
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
