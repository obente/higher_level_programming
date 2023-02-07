#!/usr/bin/python3
"""Defines object attribute and methods"""


def lookup(obj):
    """Return a list of available attributes and methods of obj."""
    return (dir(obj))
