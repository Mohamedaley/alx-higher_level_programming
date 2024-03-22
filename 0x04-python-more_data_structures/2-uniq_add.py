#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = my_list
    set(new)
    sum = 0
    for item in new:
        sum += item
return sum
