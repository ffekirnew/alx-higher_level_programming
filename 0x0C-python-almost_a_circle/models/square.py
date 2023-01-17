#!/usr/bin/python3

from rectangle import Rectangle


class Square(Rectangle):
    """Defin the class square."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] (<{self.id}>) <{self.__x}>/<{self.__y}> - <{self.__width}>/<{self.__height}>"
