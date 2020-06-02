def decorator_args(f):
    def wrapper(arg1, arg2):
        if arg1 < arg2:
            arg1,arg2 = arg2,arg1
        elif arg2 is 0:
            return "Invalid Argument"
        result = f(arg1, arg2)
        return result
    return wrapper

@decorator_args
def division(a, b):
    return a / b

print(division(2, 0))