#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    a = 0
    while (a < x):
        try:
            print("{}".format(my_list[i]), end="")
        except:
            print("")
            return a
        a += 1
    print("")
    return (a)
