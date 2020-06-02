from sys import exit

try:
    a = int(input("A: "))
    b = int(input("B: "))
except ValueError:
    print("Invalid Input")
    exit(1)

try:
    result = a / b
except ZeroDivisionError:
    print("Cannot divide by 0")
    exit(1)

print(f"{a} / {b} is {result}")