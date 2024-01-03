#!/usr/bin/python3
def fizzbuzz():
    for nim in range(1, 101):
        if nim % 3 == 0 and nim % 5 == 0:
            print("FizzBuzz", end=" ")
        elif nim % 3 == 0:
            print("Fizz", end=" ")
        elif nim % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(nim), end=" ")
