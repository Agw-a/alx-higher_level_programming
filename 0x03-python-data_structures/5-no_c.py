#!/usr/bin/python3

def no_c(my_string):
    result_string = ""
    for x in range(0, len(my_string)):
        if my_string[x] != "c" and my_string[x] != "C":
            result_string = result_string + my_string[x]
    return result_string
