""" Task1 """

# k = int(input("k: "))
# n = int(input("n: "))
#
# i = 0
# while i < n:
#     print(k)
#     i += 1

""" Task2 """

# a = int(input("a: "))
# b = int(input("b: "))
#
# x = a
# count = 0
# while x <= b:
#     print(x)
#     count += 1
#     x += 1
#
# print("Answer is:", count)

""" Task3 """

# a = int(input("a: "))
# b = int(input("b: "))
#
# x = b - 1
# count = 0
# while x > a:
#     print(x)
#     count += 1
#     x -= 1
#
# print("Answer is:", count)

""" Task4 """

# price = float(input("Price of sweet: "))
#
# kg = 1
# while kg <= 10:
#     cost = price * kg
#     print(kg, "Kg price of sweet:", cost)
#     kg += 1

""" Task5 """

# price = float(input("Price of sweet: "))
#
# kg = 0.1
# while kg <= 1:
#     cost = price * kg
#     print(kg, "Kg price of sweet:", cost)
#     kg += 0.1

""" Task6 """

# price = float(input("Price of sweet: "))
#
# kg = 1.2
# while kg <= 2:
#     cost = price * kg
#     print(kg, "Kg price of sweet:", cost)
#     kg += 0.2

""" Task7 """

# a = int(input("a: "))
# b = int(input("b: "))
#
# x = a
# sum = 0
# while x <= b:
#     sum += x
#     x += 1
#
# print("Value is:", sum)

""" Task8 """

# a = int(input("a: "))
# b = int(input("b: "))
#
# x = a
# product = 1
# while x <= b:
#     product *= x
#     x += 1
#
# print("Value is:", product)

""" Task9 """

# a = int(input("a: "))
# b = int(input("b: "))
#
# sum = 0
#
# while a <= b:
#     sum = sum + a ** 2
#     a = a + 1
#
# # Print the result
# print("The sum of squares from a to b is:", sum)

""" Task10 """

# n = int(input("Enter n: "))
#
# sum = 0
#
# i = 1
#
# while i <= n:
#     sum = sum + 1 / i
#     i = i + 1
#
# # Print the result
# print("The sum of the harmonic series up to n is:", sum)

""" Task11 """

# n = int(input("Enter n: "))
#
# sum = 0
#
# i = n
#
# while i <= 2 * n:
#     sum = sum + i ** 2
#     i = i + 1
#
# # Print the result
# print("The sum of squares from n to 2*n is:", sum)


""" Task12 """

n = int(input("Enter n: "))
product = 1

i = 1

while i <= n:
    product = product * (1.1*i)
    i = i + 1

print("The product of consecutive numbers from 1.1 to 1.1*n is:", product)
