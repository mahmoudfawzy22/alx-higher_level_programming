#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    new_dict = dict(sorted(a_dictionary.items()))
    for i, j in new_dict.items():
        print(f"'{i}' : {j}")

