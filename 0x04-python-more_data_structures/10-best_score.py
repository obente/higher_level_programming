#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    big_key = ''
    val = float('-inf')
    for k, v in a_dictionary.items():
        if v > val:
            val = v
            big_key = k
    return big_key
