#!/usr/bin/python3
"""
    This project divides each element in a list by a div value
    and returns the quotient division list
"""


def matrix_divided(matrix, div):
    """
    This function divides each element in a list and returns
    a new quotient list in two floating points precision
    """
    # cloning of list
    new_matrix = matrix[:]

    repeated_msg = "matrix must be a matrix (list of lists)\
 of integers/floats"
    # checking for empty list or none
    if not new_matrix:
        raise TypeError(repeated_msg)
    for row in new_matrix:
        # checking if nested list in having a none value
        if not row:
            raise TypeError(repeated_msg)
        # checking if nested list is not a list
        if not isinstance(row, list):
            raise TypeError(repeated_msg)
        for num in row:
            # checking if the number in list is not int or float
            if not isinstance(num, int) and not isinstance(num, float):
                raise TypeError(repeated_msg)
    # checking if the list we just cloned is a list
    if not isinstance(new_matrix, list):
        raise TypeError(repeated_msg)
        # checking if length of list is not the same
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the\
                same size")
    # checking if divisor is not int or float
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    # checking if divisor is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # applying the division
    new_list = []
    for row in new_matrix:
        fake_list = []
        for num in row:
            num = round((num / div), 2)
            fake_list.append(num)
        new_list.append(fake_list)
    return new_list
