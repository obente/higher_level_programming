#!/usr/bin/python3
"""Defines class MyList that inherits from list."""


class MyList(list):
    """Implements sorted printing inheriting from list class."""

    def print_sorted(self):
        """Print a list sorted in ascending order."""
        print(sorted(self))
