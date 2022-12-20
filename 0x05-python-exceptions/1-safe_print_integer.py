#!/usr/bin/python3
# _ _ THIS PROJECT TESTS WHETHER THE VALUE IS AN INT OR STRING
def safe_print_integer(value):
    """Checks for int or string"""
    try:
        if value > 0:
            print(value)
            return True
        elif value <= 0:
            print(value)
            return True
    except TypeError:
        return False
