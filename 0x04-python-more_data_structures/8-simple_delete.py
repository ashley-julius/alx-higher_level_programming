#!/usr/bin/python3
""" This module deletes a key in dicionary """


def simple_delete(a_dictionary, key=""):
    """ This function deletes a key in dictionary """
    for value, x in a_dictionary.items():
        if value == key:
            del a_dictionary[value]
        else:
            pass
    return a_dictionary
