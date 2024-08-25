def new_in_list(my_list, idx, element):

    if idx < 0 or idx >= len(my_list):
        return None
    else:

        new_list = my_list.copy()
        #new_list = my_list[:idx] + [element] + my_list[idx + 1:]
        
        new_list[idx] = element

    return new_list
