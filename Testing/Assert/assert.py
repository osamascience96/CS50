def square(x):
    return x * x


# These asserts line would return nothing, but if some line, where you are confident that
# its going to have a specific behaviour and you assert it but do not get, it then 
# itll throw assertion error

# Test No 1
assert square(10) == 100

# Test No 2
assert square(10) == 50