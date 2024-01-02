#!/usr/bin/python3
for a_numer in range(00, 100):
    print("{:02d}".format(a_numer), end="")
    print("", end=", " if a_numer != 99 else "\n")
