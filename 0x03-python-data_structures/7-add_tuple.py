def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 2 and len(tuple_b) == 2:
        new_tuple = tuple(a + b for a, b in zip(tuple_a, tuple_b))
        return new_tuple
    else:
        tuple_a = tuple_a + (0, 0)
        tuple_b = tuple_b + (0, 0)
        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return new_tuple

