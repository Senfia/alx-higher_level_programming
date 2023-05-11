#!/usr/bin/python3
def print_arg(argv):
    num = len(argv) - 1
    if num == 0:
        print("{:d} argument.".format(num))
        return
    else:
        if num == 1:
            print("{:d} argument:".format(num))
        else:
            print("{:d} arguments:".format(num))
        li = 1
        while i <= num:
            print("{:d}: {:s}".format(li, argv[li]))
            li += 1
if __name__ == "__main__":
    import sys
    print_arg(sys.argv)
