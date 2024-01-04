#!/usr/bin/python3
from calculator_1 import add, sub, div, mul
a = 10
b = 5
if __name__ == "__main__":
    adreslt = add(a=a, b=b)
    subreslt = sub(a=a, b=b)
    divreslt = div(a=a, b=b)
    mulreslt = mul(a=a, b=b)
    print("{} + {} = {}".format(a, b, adreslt))
    print("{} - {} = {}".format(a, b, subreslt))
    print("{} * {} = {}".format(a, b, mulreslt))
    print("{} / {} = {}".format(a, b, divreslt))
