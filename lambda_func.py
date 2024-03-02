""" ----->> <def-1> """


def welcome():
    return "Welcome"


print(welcome())

""" ----->> <lambda-1> """
wellcome = lambda: "Welcome, guys"

""" ----->> <def-2> """


def add(a, b):
    return a + b


print(add(20, 10))

""" ----->> <lambda-2> """

ad = lambda a, b: a + b
print(ad(20, 19))

S = 0
cub = lambda a,b,c: a*b*c

print(cub(10,20,10))


""" ----->> <even_or_odd - 1> """


a = int(input(">> "))

even_or_odd = lambda de: 'even' if de % 2 == 0 else 'odd'

print(even_or_odd(a))

""" ----->> <up - 1> """

up = lambda a: a.upper()
print(up("terminal"))


def add(n):
    return lambda a: a + n

result = add(10)
print(result(5))
