#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ls = len(sys.argv) - 1
    print("{:d} argument{:s}{:s}".format(ls, "s" if ls > 1 else "", "."
                                         if ls < 1 else ":"))
    for index, arg in enumerate(sys.argv[1:]):
        print("{:d}: {:s}".format(index + 1, arg))
