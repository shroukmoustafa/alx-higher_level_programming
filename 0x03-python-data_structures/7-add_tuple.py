#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple1 = (0, 0)
    tuple2 = (0, 0)
    tuple_1 = (tuple1[0] + tuple_a[0], tuple1[1] + tuple_a[1])
    tuple_2 = (tuple2[0] + tuple_b[0], tuple2[0] + tuple_b[1])
    new_tuple = (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])
    return new_tuple