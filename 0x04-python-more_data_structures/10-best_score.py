#!/usr/bin/python3

def best_score(a_dictionary):
    if isinstance(a_dictionary, dict) and a_dictionary != {}:
        big_key = ''
        val = float('-inf')
        for k, v in a_dictionary.items():
            if v > val:
                val = v
                big_key = k
        return big_key
    return None
