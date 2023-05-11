#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv) - 1
    if (args == 0):
        print("{:d} arguments.".format(args))
    elif (args == 1):
        print("{:d} argument:".format(args))
    else:
        print("{:d} arguments:".format(args))
    for str in range(len(sys.argv)):
        if (str == 0):
            continue
        print("{:d}: {:s}".format(str, sys.argv[str]))
