#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        max_list = my_list[0]
        for x in my_list:
            if x > max_list:
                max_list = x
        return max_list