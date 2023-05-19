#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    if my_list:
        my_list.sort()
        sum += my_list[0]
        for n in range(1, len(my_list)):
            viewd = False
            if my_list[n - 1] == my_list[n]:
                viewd = True
            if not viewd:
                sum += my_list[n]
    return sum
