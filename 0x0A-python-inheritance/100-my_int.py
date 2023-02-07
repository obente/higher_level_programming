#!/usr/bin/python3
"""Defines class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operator == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != operator behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == operator behavior."""
        return self.real == value
