#!/usr/bin/python3

class Square:
    """Define sq,"""
    def __init__(self, size=0):
        """
            size:length of sq.Dafault to 0
            raise error if not an integer
         """
        if type(size) is nit int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size__ = size
