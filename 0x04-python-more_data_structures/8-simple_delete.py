#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if key == 'None':
        return
    else:
        del a_dictionary[key]
