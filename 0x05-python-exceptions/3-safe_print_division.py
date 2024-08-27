#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        num = a / b
    except ZeroDivisionError:
        num = None
    finally:
        print("inside result: {}".format(num))
        return num