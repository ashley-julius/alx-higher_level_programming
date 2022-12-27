#!/usr/bin/python3
"""This module defines a Square"""


class Square():
    """
        Square: defines a square
        Attributes:
                size: To know the length of sides, area and perimeter

        Method:
                __init__: Initializing the Square attribute

                area: Calculates the area of square
     """
    def __init__(self, size=0, position=(0, 0)):
        """Initializing the instance attribute

        Args:
            Size attributes
            position attributes
        """
        self.__size = size
        self.__position = position
    # Using property decorator
    # a getter function

    @property
    def size(self):

        """
            size: to return the size attribute
        """
        return self.__size
    # setter function

    @size.setter
    def size(self, value):
        """
            size: To set the size attribute

            Arguments:
                value: an integer or string
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    # getters function
    def position(self):
        """
            position: retrieves the position
        """
        return self.__position

    @position.setter
    # setter function
    def position(self, value):
        """
            position: sets the position attributes
            Argument:
                value: instance attribute
        """
        if value[0] < 0 and value[1] < 0:
            raise TypeError("position must be a tuple of 2\
 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2\
 positive integers")
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2\
 positive integers")

    def area(self):
        """Calculates the area of square"""
        return (self.__size ** 2)

    def my_print(self):
        """
            my_print: prints # or blank line to stdout
        """
        if self.__size == 0:
            print("")
        else:
            for line in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                if self.__position[0] != 0:
                    for space in range(0, self.__position[0]):
                        print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
