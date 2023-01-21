#!/usr/bin/python3

from rectangle import Rectangle


class Square(Rectangle):
    """Defin the class square."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Return the size of the square."""
        return self.__size

    @size.setter
    def size(self, size):
        """Set the values of the square."""
        self.size = self.__validator("size", size)
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Updates all attributes of the rectangle."""
        if args:
            id, size, x, y = args
            self.id = id
            self.size = size
            self.x = x
            self.y = y
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Return dictionary representaion of the Rectangle."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        return f"[Square] (<{self.id}>) <{self.__x}>/<{self.__y}> - <{self.__width}>/<{self.__height}>"
