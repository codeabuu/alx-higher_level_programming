#!/usr/bin/python3
"""This module inherits from list class"""


class MyList(list):
    """A class that inherits from list"""
    def print_sorted(self):
        """The method which prints sorted list in ascending"""
        sorted_ls = sorted(self)
        print(sorted_ls)
