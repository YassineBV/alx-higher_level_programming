#!/usr/bin/python3
for asci in range(122, 96, -1):
    print("{}".format(chr(asci)) if asci % 2 == 0 else "{}".format(chr(asci - 32)), end="")

