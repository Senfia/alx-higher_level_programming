#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tuple_a = 0, 0
    if len(tuple_b) == 0:
        tuple_b = 0, 0
    if len(tuple_a) == 1:
        tuple_a = tuple_a[0], 0
    if len(tuple_b) == 1:
        tuple_b = tuple_b[0], 0

    result = []
    for index in range(2):
        if tuple_a[index] == "None":
            first_value = 0
        else:
            first_value = tuple_a[index]
        if tuple_b[index] == "None":
            second_value = 0
        else:
            second_value = tuple_b[index]
        result.append(first_value + second_value)

    return (result[0], result[1])
