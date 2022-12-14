#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1 if (number > 0) else -1
last_digit = ((sign * number) % 10) * (sign)
print("Last digit of {} is {} and is".format(number, last_digit), end=" ")
if (last_digit == 0):
    print(0)
elif (last_digit < 6):
    print("less than 6 and not 0")
else:
    print("greater than 5")
