#!/usr/bin/python3

from xxlimited import new


def divisible_by_2(my_list=[]):
    new_list = []

    for y in my_list:
        if y % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
