#!/usr/bin/python3

def add_integer(a, b=98):
    """ function to add two integers """
    
    """ Raises a Typeerror if values passed is not an int or float"""
    if type(a) not in (int, float):
        raise TypeError("You didnt enter an integer or float")
    if type(b) not in (int, float):
        raise TypeError("{} not an integer or float".format(b))
    return int(a) + int(b)

