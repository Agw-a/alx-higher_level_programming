#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    a function to find the peak in an unsorted list of ints
    """
    idx = len(list_of_integers) - 1

    if list_of_integers == []:
        return None
    for n in range(1, idx):
        if list_of_integers[n + 1] < list_of_integers[n]\
        and list_of_integers[n - 1] < list_of_integers[n]:
            return list_of_integers[n]
    return (max(list_of_integers[0], list_of_integers[-1]))
       
