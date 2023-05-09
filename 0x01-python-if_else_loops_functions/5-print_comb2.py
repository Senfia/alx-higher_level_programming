#!/usr/bin/python3
for nm in range(100):
    if (nm != 99):
        print("{:02d}".format(nm), end=", ")
    else:
        print("{:02d}".format(nm))
