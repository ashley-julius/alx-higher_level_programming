#!/usr/bin/python3
""" This module deletes keys with a specific value """


def complex_delete(a_dictionary, value):
    """ This function deletes keys with specific values """
    # create a copy
    find_to_dele = dict(list(a_dictionary.items())[:])
    # check if value to delete is not none and type is a dict
    if find_to_dele is not None and type(find_to_dele) is dict:
        # iterate the tuple given by item(key, val)
        for (key, val) in find_to_dele.items():
            # check if it is the value to delete
            if value == val:
                # if it is, create a new dict
                dele_dict = {key: val}
            # iterate and delete the keys
                for (key, val) in dele_dict.items():
                    del find_to_dele[key]
        # return a copy when we are done
        return find_to_dele
