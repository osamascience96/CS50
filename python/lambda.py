people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]


people.sort(key=lambda person: person["name"])

print(people)


def build_quadratic_function(a, b, c):
    return lambda x: a*x**2 + b*x + c

f = build_quadratic_function(2, 3, -5)

print(f(2))