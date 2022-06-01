#!/usr/bin/python3
def remove_char_at(str, n):
    cpy = ""
    for ch in range(0, len(str)):
        if ch != n:
            cpy += str[ch]
    return cpy
