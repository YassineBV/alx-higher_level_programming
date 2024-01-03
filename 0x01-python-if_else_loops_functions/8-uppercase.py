#!/usr/bin/python3
def uppercase(str):
    for charc in str:

        print("{}".format(chr(ord(charc) - 32)) if ord(charc) in range(97, 123) else "{}".format(charc), end="")
    print()
