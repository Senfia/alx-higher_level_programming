#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    c = 0
    while c < x:
        try:
            print("{}".format(my_list[c]), end="")
        except (IndexError, TypeError):
            break
        c += 1
    print("")
    return (c)
