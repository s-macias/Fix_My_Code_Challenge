#!/usr/bin/python3
""" Class Square """


class Square():
    """ Class Square """
    width = 0
    height = 0

    def __init__(self, width, height):
        """ defining Square class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Private instance attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value

    @property
    def height(self):
        """ Private instance attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.height = value

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ returns perimeter of the square """
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """ returns a string representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=12)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
