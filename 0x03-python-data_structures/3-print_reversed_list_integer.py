#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    x = len(my_list)
    for i in my_list:
        if x > 0:
            x = x - 1
            print("{:d}".format(my_list[x]))
