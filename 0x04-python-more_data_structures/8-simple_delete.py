#!/usr/bin/python3
""" This module deletes a key in dicionary """


def simple_delete(a_dictionary, key=""):
    """ This function deletes a key in dictionary """
    b_dictionary = dict(list(a_dictionary.items())[:])
    if key is not "" and key in b_dictionary:
        b_dictionary.pop(key)
    return b_dictionary
