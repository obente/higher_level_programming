#!/usr/bin/python3

""" Define class called Square """


class Square:
    """ Square class which does nothing """
    def __init__(self, size=0):
        """ Initialize square """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
