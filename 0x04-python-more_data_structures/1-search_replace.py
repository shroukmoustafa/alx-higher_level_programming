#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == []:
        return my_list
    for i in range(len(my_list)):
        new_list = [replace if x == search else x for x in my_list]
    return new_list
