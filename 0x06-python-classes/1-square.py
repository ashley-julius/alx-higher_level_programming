#!/usr/bin/python3
# _ _ _ THIS PROGRAM PROVIDES MORE INSIGHT ON OOPS


class Square:
    """
        square: defines a square
        Attributes:
            size: To know the length of side, area and perimeter
        Method:
                __init__: To Initialize the instance variable
    """
    def __init__(self, size):
        """Initializing the attributes
            Args:
                size attributes
        """
        self.__size = size
