def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            int(my_list[i])

        except ValueError:
            continue
