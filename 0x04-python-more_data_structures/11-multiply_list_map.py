#!/usr/bin/python3
""" This module returns a list with values multiplied without using
    loops
"""


def multiply_list_map(my_list=[], number=0):
    """ This function multiplies a list without using loop """
    return (list(map(lambda x: x * number, my_list)))
