from sys import stderr
def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception :{}".format(e), file=stderr)
        return None