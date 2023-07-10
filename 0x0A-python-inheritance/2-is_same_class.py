#!/usr/bin/python3
"""Checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """will returns True if the object is exactly
    an instance of the specified class"""
    return (type(obj) is a_class)
