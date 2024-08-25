def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        #new_list = my_list[0:idx] + my_list[idx+1:]
        del my_list[idx]
        return my_list