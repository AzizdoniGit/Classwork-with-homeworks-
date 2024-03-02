# def numbers(*n):
#     res = []
#     for i in n:
#         res.append(i**2)
#     return res
# print(numbers(6))


# def upperCase(*args: str):
#     result = []
#     for i in args:
#         result.append(i.upper())
#     return result
#
#
# print(upperCase("hello", "freak"))


# def summ(*args: int):
#     result = 0
#     for i in args:
#         result += i
#     return result
#
#
# print(summ(10, 20, 30, 40))

"""
  Task
"""
# def multiplyS(*args: int):
#     result = 1
#     for i in args:
#         result *= i
#     return result
#
#
# print(multiplyS(10, 20, 30, 40))


"""
  Task
"""


# def sum_even_and_odd(*args: int):
#     even = 0
#     odd = 0
#     for i in args:
#         if i % 2 == 0:
#             even += i
#         elif i % 2 == 1:
#             odd += i
#         else:
#             print("Error")
#     return even, odd


# a, b = sum_even_and_odd(20, 30, 40, 10, 5, 3, 2)
# print("Even >>", a)
# print("Odd >>", b)


def sum_even_and_odd(*args: int):
    even = 0
    odd = 0
    for i in args:
        if i / i == 1 and i / 1 == i:
            even = i
        if i / i == 1 or i / 1 == i or i / 5 or i / 2 or i / 3 or i / 4:
            odd = i

    return even, odd


a, b = sum_even_and_odd(5, 30, 10, 1)
print("Even >>", a)
print("Odd >>", b)
