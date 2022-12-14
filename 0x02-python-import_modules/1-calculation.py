#!/usr/bin/python3
# _ _ _ _ HANDS ON EXPERIENCE WITH MODULES _ _ _ _ _
if __name__ == "__main__":
    import calculator_1
    """Defining the two integers"""
    a = 10
    b = 5

    """Calling the Addition Function"""
    print("{:d} + {:d} = {:d}".format(a, b, calculator_1.add(a, b)))

    """Calling the Subtraction Function"""
    print("{:d} - {:d} = {:d}".format(a, b, calculator_1.sub(a, b)))

    """Calling the Multiplication Function"""
    print("{:d} * {:d} = {:d}".format(a, b, calculator_1.mul(a, b)))

    """Calling the Division Function"""
    print("{:d} / {:d} = {:d}".format(a, b, calculator_1.div(a, b)))
