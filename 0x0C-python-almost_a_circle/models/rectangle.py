#!/usr/bin/python3

"""Module with class Rectangle that inherits from Base"""

from models.base import Base


class Rectangle(Base):
    """Defining Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize class"""
        super().__init__ = (id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            """getting width"""
            return self.__width

        @property
        def height(self):
            """heigtht getter"""
            return self.__height

        @propery
        def x(self):
            """getting x"""
            return self.__x

        @property
        def y(self):
            """y getter"""
            return self.__y

        """Validating with setter methods"""

        @width.setter
        def width(self, value):
            """setting width"""
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @height.setter
        def height(self, value):
            """setting height"""
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @x.setter
        def x(self, value):
            """setting width"""
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @y.setter
        def y(self, value):
            """setting width"""
            if type(value) is not int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """Returns area value of rectangle instance"""
            return self.__width * self.__height

        def display(self):
            """Prints to the stdout Rectangle instance with '#'"""
            for j in range(self.__y):
                print()
            for j in range(self.__height):
                for x in range(self.__x):
                    print(" ", end="")
                for i in range(self.__width):
                    print('#', end="")
                print()

        def __str__(self):
            """return string of object"""
            return "[Rectangle] ({}) {}/{} - {}/{}"\
                .format(self.id, self.__x, self.__y, self.__width, self.__height)

        def update(self, *args, **kwargs):
        """ updates the instance attributes:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        count = 0
        if args != ():
            for a in args:
                count += 1
                if count == 1:
                    self.id = a
                if count == 2:
                    self.width = a
                if count == 3:
                    self.height = a
                if count == 4:
                    self.x = a
                if count == 5:
                    self.y = a
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        newd = dict()
        newd["id"] = self.id
        newd["width"] = self.width
        newd["height"] = self.height
        newd["x"] = self.x
        newd["y"] = self.y
        return newd
