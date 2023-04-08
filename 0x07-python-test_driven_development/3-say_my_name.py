#!/usr/bin/python3
'''
This module prints full names of persons
'''


def say_my_name(first_name, last_name=""):
    '''
    returns full name when given first_name and last_name

    Args:
    first_name (str): firstname of person
    last_name (str): lastname of person

    Raises:
    TypeError: if argument passed is not of type str

    Returns:
    (str): concatenated first_name and last_name with additional text
    '''

    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    return f"My name is {first_name} {last_name}"
