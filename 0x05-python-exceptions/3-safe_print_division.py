#!/usr/bin/python3
# _ _ THIS PROJECT SHOWS US HOW TO HANDLE THE ZeroDivisionError
def safe_print_division(a, b):
    """Shows how to handle ZeroDivisionError"""
    quotient = 0
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
    return quotient
