def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0 :
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError(" size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")

if __name__ == "__main__":
    import doctest
    doctest.testfile("4-print_square.txt")