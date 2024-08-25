def max_integer(my_list=[]):
    ma = 0
    for i in my_list:
        if i > ma:
            ma = i
        else:
            continue
    
    return ma