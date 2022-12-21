#!/usr/bin/python3
"""This module contains the class square
"""


class Square:
    '''This is class defines a squre with the given size
    '''
    def __init__(self, size=0):
        '''This constructor will initialize the class with the given
        size or will give it the default value 0.
        Args:
            size (int): The size for the square
        '''
        try:
            size = int(size)
            if size < 0:
                raise ValueError("size must be >= 0")
            self.size = size
        except TypeError as e:
            raise e("size must be an integer")

    def area(self):
        '''This method will return the current area of the
        given square instance
        '''
        return self.__size ** 2

    def my_print(self):
        '''Prints the given square with the sign #
        '''
        if not self.size:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print('#', end='')
            print()

    @property
    def size(self):
        '''Getter for size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' sets a value for the private variable size
        '''
        try:
            value = int(value)
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        except TypeError as e:
            raise e("size must be an integer")
