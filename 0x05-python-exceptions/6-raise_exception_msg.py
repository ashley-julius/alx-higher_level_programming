#!/usr/bin/python3
# THIS PROJECT SHOWS US A MORE ADVANCED WAY OF RAISING AN EXCEPTION
def raise_exception_msg(message=""):
    """This project shows how to raise an exception
    with a message
    """
    try:
        raise NameError
    except NameError:
        print(message)   
