#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            bool_list[i] = True
        else:
            bool_list[i] = False
    return bool_list
