#!/usr/bin/python3
# _ _ _ _ BUILDING MY OWN CALCULATOR _ _ _ _
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, a, b, mul, div
    operators = ['+', '-', '*', '/']
    # _ _ _ CHECKING IF THE ARGUMENTS SUM UP TO THREE
    if len(sys.argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        return 1

    # _ _ CHECKING IF THE ANY OF THE OPERATORS IS IN SYS.ARGV
    argu_ment = sys.argv[:]
    if argu_ment[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        return 1
    # _ _ COLLECTING THE TWO VALUES AND THE OPERATOR TO USE _ _
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # _ _ _ RETURN WHICH FUNCTION BASED ON THE OPERATOR FOUND  _ _ _ _
    match argu_ment[2]:
        case "+":
            print("{:d} + {:d} = {:d}".format(a, b, (add(a, b))))
        case "-":
            print("{:d} - {:d} = {:d}".format(a, b, (sub(a, b))))
        case "*":
            print("{:d} * {:d} = {:d}".format(a, b, (mul(a, b))))
        case _:
            print("{:d} / {:d} = {:d}".format(a, b, (div(a, b))))
