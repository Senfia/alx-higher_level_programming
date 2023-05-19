#!/usr/bin/python3

def search_replace(my_list, search, replace):
    item = []
    if my_list:
        for n in my_list:
            if not n == search:
                item.append(n)
            else:
                item.append(replace)
    return item
