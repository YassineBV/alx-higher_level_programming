#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for indx in range(list_length):
        try:
            elm = my_list_1[indx] / my_list_2[indx]
        except ZeroDivisionError:
            elm = 0
            print("division by 0")
        except TypeError:
            elm = 0
            print("wrong type")
        except IndexError:
            print("out of range")
            elm = 0
        finally:
            my_list_3.append(elm)
    return my_list_3
