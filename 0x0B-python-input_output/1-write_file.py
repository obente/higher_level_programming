#!/usr/bin/python3
"""Function to write UTF8 textfile"""


def write_file(filename="", text=""):
    """ Write a file and return number of string written

    Keyword argumwnts
    filename - file to be write to (defaults to empty string)
    text - string content to write (defaults to empty string)
    """
    with open(filename, 'w') as f:
        return (f.write(text))
