#!/usr/bin/python3
# _ _ _ THIS PROJECT RETURNS THE AMOUNT OF KEYS IN A DICTIONARY _ _ _
def number_keys(a_dictionary):
    sum = 0
    for key in a_dictionary.keys():
        sum += 1
    return sum
