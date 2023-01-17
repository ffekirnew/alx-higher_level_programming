#!/usr/bin/python3
"""Contains class definition for the class Base."""


from base import Base


class Rectangle(Base):
    """Define the class rectnagle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize an instance of the class Rectangle."""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for width."""
        self.__width = self.__validator("width", width)

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter for height."""
        self.__height = self.__validator("height", height)

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter for x."""
        self.__x = self.__validator("x", x)

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter for y."""
        self.__y = self.__validator("y", y)

    def __validator(self, name, value):
        """Validates inputs with the given guideline."""
        if type(value) is str:
            raise TypeError(f"{name} must be an integer")
        elif (name == "width" or name == "height") and value <= 0:
            raise TypeError(f"{name} must be > 0")
        elif (name == "x" or name == "y") and value < 0:
            raise TypeError(f"{name} must be >= 0")
        return value

    def area(self):
        """Return the area of the REctangle."""
        return self.__width * self.__height

    def display(self):
        """Print the rectangle with '#'."""
        for z in range(self.__y):
            print()
        for i in range(self.__height):
            for y in range(self.__x):
                print(" ", end='')

            for j in range(self.__width):
                print('#', end='')
            print()

    def update(self, *args, **kwargs):
        """Updates all attributes of the rectangle."""
        if args:
            id, width, height, x, y = args
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y
            self.id = id
        else:
            if "id" in kwargs:
                self.id = id
            if "width" in kwargs:
                self.__width = width
            if "height" in kwargs:
                self.__height = height
            if "x" in kwargs:
                self.__x = x
            if "y" in kwargs:
                self.__y = y

    def __str__(self):
        return f"[Rectangle] (<{self.id}>) <{self.__x}>/<{self.__y}> - <{self.__width}>/<{self.__height}>"
