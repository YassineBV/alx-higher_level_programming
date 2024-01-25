#!/usr/bin/python3
def safe_print_division(a, b):
    reslt = None
    try:
        reslt = a / b
    except ZeroDivisionError:
        reslt = None
    finally:
        print("Inside result: ", reslt)
        return reslt

