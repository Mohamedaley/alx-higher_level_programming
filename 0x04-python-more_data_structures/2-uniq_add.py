#!/usr/bin/python3

def uniq_add(my_list=[]):
    new = []
    sum = 0
    for item in my_list:
        if item not in new:
            sum += item
            new.append(item)
    return sum
