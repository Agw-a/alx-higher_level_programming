#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        if ord(ch) >= 97 and ord(ch) <= 122:
            upp_er = ord(ch) - 32
        else:
            upp_er  = ord(ch)
        print("{:c}".format(upp_er), end="")
    print("")
    