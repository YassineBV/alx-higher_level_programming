#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        print("{}".format(abs(number) % 10) * -1, end="")
        return number
    elif number == 0:
        print("{}".format(number), end="")
        return number
    else:
        number = number % 10
        print("{}".format(number), end="")
        return number
