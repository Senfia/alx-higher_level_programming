#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return (0)
    final = sum(number[0] * number[1] for number in my_list)
    final /= sum(number[1] for number in my_list)
    return final
