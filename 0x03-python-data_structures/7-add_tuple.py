#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple1 = ()
    tuple2 = ()
    for i in range(0, 2):
        if not tuple_a[i]:
            tuple1 += (0,)
        else:
            tuple1 += tuple_a[i]
        if not tuple_b[i]:
            tuple2 += (0,)
        else:
            tuple2 += tuple_b[i]
    new_tuple = (tuple_1[0] + tuple_2[0], tuple_1[1] + tuple_2[1])
    return new_tuple
