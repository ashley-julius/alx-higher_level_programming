#!/usr/bin/python3
# _ _ _ _ HANDS ON EXPERIENCE WITH MODULES _ _ _ _ _
if __name__ == "__main__":
    import calculator_1
    """Defining the two integers"""
    a = 10
    b = 5

    """Calling the Addition Function"""
    add = calculator_1.add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, add))

    """Calling the Subtraction Function"""
    diff = calculator_1.sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, diff))

    """Calling the Multiplication Function"""
    mult = calculator_1.mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, mult))

    """Calling the Division Function"""
    div = calculator_1.div(a, b)
    print("{:d} / {:d} = {:d}".format(a, b, div))
