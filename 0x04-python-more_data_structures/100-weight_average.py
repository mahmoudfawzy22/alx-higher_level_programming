#!/usr/bin/python3
def weight_average(my_list=[]):
    result = sum(score * wight for score, wight in my_list)
    wights = sum(wight for _, wight in my_list)

    return result / wights