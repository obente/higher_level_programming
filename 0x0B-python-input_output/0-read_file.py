#!/usr/bin/python3
"""Function to read UTF* textfile"""


def read_file(filename=""):
    """ Read a file and print to stdout
    
    Keyword argumwnts
    filename - file to be read (defaults to empty string
    """
    with open(filename, encoding="utf-8") as f:
        read_data = f.read()
    
    print(read_data)

