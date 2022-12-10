#!/usr/bin/python3
#  _ _ _ THIS PROJECT REPLACES A VALUE OR ADDS A KEY AND VALUE _ _ _
def update_dictionary(a_dictionary, key, value):
    newlist = list(a_dictionary)
    if key in newlist:
        a_dictionary[key] = value
    if key not in newlist:
        a_dictionary[key] = value
    return a_dictionary
