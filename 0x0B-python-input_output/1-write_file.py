#!/usr/bin/python3
"""This module defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file
    """
    file = open(filename, "a", encoding="utf-8")
    return file.write(text)
