#!/usr/bin/python3
"""
Square mod.
"""


class Square:
    """
    defines sq. by length, size.
    must be an integer and non negative.
    """
    def __init__(self, size=0):
        """
        Derfine length and area
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size__ = size

    @property
    def size(self):
        """
            Retreive  value of __size
        """
        return self.__size

    @size.setter
    def size(self, value):

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size__ = value

    def area(self):
        return self.__size ** 2
