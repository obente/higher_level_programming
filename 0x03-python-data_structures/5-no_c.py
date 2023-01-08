#!/usr/bin/python
def no_c(my_string):
    x = ""
    for letter in my_string:
        if 'c' == letter or 'C' == letter:
            continue
        x = x+letter
    return x
