#!/usr/bin/python3
"""This class represents a rectangle with attributes for length and width."""


class Rectangle:
    """Class that defines a rectangle by width and height"""
    
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property 
    def width(self):
        """Retrieve the width of the rectangle""" 
        return self.__width

    @width.setter 
    def width(self, value): 
        """Set the width of the rectangle""" 

        if type(value) is not int:  # Check if value is an integer or not  
            raise TypeError("width must be an integer") # Raise exception if value is not an integer 

        if value < 0: # Check if value is greater than 0 or less than 0 
            raise ValueError("width must be >= 0") #Raise exception if value is less than 0

        self.__width = value # Set the value to the private instance attribute __width otherwise  

    @property 
    def height(self):  
        """Retrieve the height of the rectangle""" 

        return self.__height  

    @height.setter  
    def height(self, value):  

        """Set the height of the rectangle"""  

        if not isinstance(value, int): # Check if value is an integer or not  
            raise TypeError("height must be an integer") # Raise exception if value is not an integer

        if value < 0: # Check if value is greater than 0 or less than 0    
            raise ValueError("height must be >= 0") #Raise exception if value is less than 0    

        self.__height = value
