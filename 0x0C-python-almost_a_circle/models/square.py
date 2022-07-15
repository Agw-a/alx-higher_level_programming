#!/usr/bin/python3

"""Module with Square that inherits from Rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """defdining square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializing"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string method rep of object"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ updates attributes of square """
        if args != ():
            if len(args) >= 2:
                newargs = args[0:2] + args[1:]
            else:
                newargs = args
            super().update(*newargs)
        else:
            newkwargs = dict()
            for k, v in kwargs.items():
                if k == "size":
                    newkwargs["width"] = v
                    newkwargs["height"] = v
                else:
                    newkwargs[k] = v
            super().update(**newkwargs)

    def to_dictionary(self):
        """ returns dictionary representation of a Square """
        ds = super().to_dictionary()
        ds["size"] = ds["height"]
        del ds["height"]
        del ds["width"]
        return ds
