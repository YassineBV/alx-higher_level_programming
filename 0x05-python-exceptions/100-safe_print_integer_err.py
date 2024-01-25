#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    bool = None
    try:
        print("{:d}".format(value))
        bool = True
    except ValueError as message:
        bool =  False
        print("Exception: {}".format(message), file=sys.stderr)
    finally:
        return bool
