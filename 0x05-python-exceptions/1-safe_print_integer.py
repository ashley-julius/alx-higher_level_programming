#!/usr/bin/python3
# _ _ THIS PROJECT TESTS WHETHER THE VALUE IS AN INT OR STRING
def safe_print_integer(value):
    """Checks for int or string"""
    try:
            print("{:d}".format(value))
            return True
    except ValueError:
        return False
