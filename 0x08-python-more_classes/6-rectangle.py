#!/usr/bin/python3
"""This class represents a rectangle with attributes for length and width."""


class Rectangle:
    """Class that defines a rectangle by width and height."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiate with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if type(value) is not int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__height and self.__width:
            return (2 * self.__height + 2 * self.__width)
        return 0

    def __str__(self):
        """Return string representation of the object."""
        string = ""
        if (self.area() != 0):
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    string += "#"
                string += "\n"
            return string
        else:
            return ""

    def __repr__(self):
        """Return a string representation of the
        object so it can be recreated by using eval().
        """
        return "Rectangle({}, {})".format(str(self.width), str(self.height))

    def __del__(self):
        """Execute when a del keyword is called upon an instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        return None
