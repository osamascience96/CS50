def announce(f):
    def wrapper():
        print("Going to do something before the function")
        f()
        print("Done the work for the function")
    return wrapper


@announce
def hello():
    print("Hello World")

hello()