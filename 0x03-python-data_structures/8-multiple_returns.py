#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    t = (0,)
    if sentence:
        first = sentence[0]
        t = (t[0] + length, first)
        return t
    t = (t[0], 'None')
    return t
