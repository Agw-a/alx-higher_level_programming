#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = abs(number) % 10
out_put = "Last digit of"
if number < 0:
    lastDigit = -lastDigit
print("{} {} is {} and is ".format(out_put, number, lastDigit), end="")
if lastDigit > 5:
    print("greater than 5")
if lastDigit == 0:
    print("0")
else:
    print("less than 6 and not 0")
