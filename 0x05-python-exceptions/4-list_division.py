#!/usr/bin/python3
# THIS PROJECT SHOWS HOW TO HANDE TYPEERROR, ZERODIVISION AND MORE
def list_division(my_list_1, my_list_2, list_length):
    """This project shows how to handle multiple exceptions"""
    Quotients = []
    for i in range(0, list_length):
        quotient = 0
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except TypeError:
            quotient = 0
            print("wrong type")
        except ZeroDivisionError:
            quotient = 0
            print("division by 0")
        except IndexError:
            quotient = 0
            print("out of range")
        finally:
            Quotients.append(quotient)

    return Quotients    
