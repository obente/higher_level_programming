#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_tuple_1 = tuple_a + (0, 0)
    my_tuple_2 = tuple_b + (0, 0)
    a = my_tuple_1[0] + my_tuple_2[0]
    b = my_tuple_1[1] + my_tuple_2[1]
    return (a, b)
