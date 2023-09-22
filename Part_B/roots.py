import math

def find_roots(a, b, c):
    disc = b**2 - 4*a*c
    if disc > 0:
        root1 = (-b + math.sqrt(disc)) / (2*a)
        root2 = (-b - math.sqrt(disc)) / (2*a)
        return root1, root2
    elif disc == 0:
        root = -b / (2*a)
        return root
    else:
        return "No real roots"

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

roots = find_roots(a, b, c)
print("Roots:", roots)