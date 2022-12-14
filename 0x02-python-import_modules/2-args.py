#!/usr/bin/python3
# _ _ _ THIS PROJECT SHOWS HOW TO WORK WITH COMMANDLINE ARGUMENTS
if __name__ == "__main__":
    import sys

    # _ _ _ _TOTAL ARGUMENTS
    n = len(sys.argv)
    # _ _ _ CHECK IF N IS 0, 1 OR > 1
    if n > 1:
        print("{:d} arguments:".format((n - 1)))
    elif n == 1:
        print("{:d} argument:".format((n - 1)))
    elif n == 0:
        print("{:d} arguments.".format(n))
    for i in range(1, len(sys.argv)):
        print("{:d}: {}".format(i, sys.argv[i]))
