'''
This module prints full names of persons
'''

def say_my_name(first_name, last_name=""):
    '''
    returns full name when given first_name and last_name
    '''

    if not (isinstance(first_name, str) and isinstance(last_name, str)):
        raise TypeError("first_name must be a string or last_name must be a string")
    return f"My name is {first_name} {last_name}"

