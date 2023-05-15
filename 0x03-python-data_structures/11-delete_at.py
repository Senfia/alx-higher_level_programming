#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    return (my_list.remove(my_list[idx]) if not 
    (idx > len(my_list) - 1 or idx < 0) else my_list)
