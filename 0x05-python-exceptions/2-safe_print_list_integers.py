#!/usr/bin/python3
# THIS PROJECT SHOWS HOW TACKLE AN EXCEPTION IN SILENCE

def safe_print_list_integers(my_list=[], x=0):
    """Pass any value that is not an int"""
    count = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count += 1
        except TypeError:
            pass
        except ValueError:
            pass
    print()
    return count
