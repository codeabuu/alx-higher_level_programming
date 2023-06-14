#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_ls = set(my_list)
    num = 0
    for i in uniq_ls:
        num += i
    return (num)
