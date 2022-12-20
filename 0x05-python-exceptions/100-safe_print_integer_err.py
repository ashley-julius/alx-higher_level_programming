#!/usr/bin/python3
import sys
# THIS PROJECT SHOW HOW TO PRINTING IMMEDIATE ERROR MESSAGES TO STDERR


def safe_print_integer_err(value):
    """Display message to stderr if an exception occurs"""
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        print("Exception: Unknown format code 'd' for object of type\
 'str'", file=sys.stderr)
        return False
