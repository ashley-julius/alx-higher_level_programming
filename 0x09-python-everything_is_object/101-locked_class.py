#!/usr/bin/python3
"""This module allows only attribute called first_name"""


class LockedClass:
    """This class has no class or object attributes, it only prevents
    the user from dynamically creating new instance attribute not
    called first_name
    """
    __slots__ = ["first_name"]
