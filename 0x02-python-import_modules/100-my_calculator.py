#!/usr/bin/python3
from sys import argv
import calculator_1
if __name__ == "__main__":
    arglen = len(argv)
    if arglen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:

        toint1 = int(argv[1])
        toint2 = int(argv[3])
        adreslt = calculator_1.add(toint1, toint2)
        subreslt = calculator_1.sub(toint1, toint2)
        divreslt = calculator_1.div(toint1, toint2)
        mulreslt = calculator_1.mul(toint1, toint2)
        if argv[2] == '+':
            print("{} + {} = {}".format(toint1, toint2, adreslt))
        elif argv[2] == '-':
            print("{} - {} = {}".format(toint1, toint2, subreslt))
        elif argv[2] == '*':
            print("{} * {} = {}".format(toint1, toint2, mulreslt))
        elif argv[2] == '/':
            print("{} / {} = {}".format(toint1, toint2, divreslt))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
