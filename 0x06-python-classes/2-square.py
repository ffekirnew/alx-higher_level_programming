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
            self.__size = size
        except TypeError as e:
            raise e("size must be an integer")
