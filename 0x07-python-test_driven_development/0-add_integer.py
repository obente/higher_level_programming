#!/usr/bin/python3

def add_integer(a, b=98):
    """ function to add two integers """
    
    """ Raises a Typeerror if values passed is not an int or float"""
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
