#!/usr/bin/python3
# _ _ THIS PROJECT PRINTS THE KEYS IN A DICTIONARY IN SORTED ORDER _ _
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
