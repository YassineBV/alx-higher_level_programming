#!/usr/bin/python3
def multiple_returns(sentence):
    my_tup = (0, 0)
    my_tup = (len(sentence), sentence[0] if len(sentence) > 0 else None)
    return my_tup
