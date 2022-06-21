#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):

    count = 0
    try:
        for lst in range (x):
            print("{}".format(my_list[lst]), end="")
            count += 1
        print()
    except:
        print()
        return count
    return count
