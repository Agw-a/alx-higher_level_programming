#!/usr/bin/python3
for alph in range(122, 96, -1):
    if i % 2 == 0:
        print("{:c}".format(alph), end="")
    else:
        print("{:c}".format(alph - 32), end="")
