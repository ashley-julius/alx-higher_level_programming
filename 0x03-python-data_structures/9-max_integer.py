#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        maximum = 0
        for i in my_list:
            if i > maximum:
                maximum = i
        return maximum
