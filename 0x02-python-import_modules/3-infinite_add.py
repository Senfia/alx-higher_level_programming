#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print('{:d}'.format(sum(int(i) for i in sys.argv[1:])))
