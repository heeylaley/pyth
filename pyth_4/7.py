from math import factorial


def fact(n):
    generator = [num + 1 for num in range(n)]
    for el in generator:
        yield el


for i in fact(7):
    print(factorial(i))
