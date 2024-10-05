"""
This file for add two integer
for example a = 5 and b = 10
result = 15
"""

def add_integer(a, b=98):
    '''add two integer
    args: a first integer
    b: second integer'''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")