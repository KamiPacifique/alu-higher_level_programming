#!/usr/bin/python3
"""
Module that defines a class MyList inheriting from list.
"""

class MyList(list):
    """
    MyList class that extends the built-in list class
    with a method to print a sorted version of the list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        print(sorted(self))
