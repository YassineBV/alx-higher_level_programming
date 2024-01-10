#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unq_set1 = set(set_1)
    unq_set2 = set(set_2)
    return unq_set1 ^ unq_set2
