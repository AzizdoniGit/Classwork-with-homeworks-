"""               """
"""   Function 1  """
"""               """

# def hi():
#     print("Good evening")
#
# hi()

"""               """
"""   Function 2  """
"""               """

# def abc():
#     tmp = []
#     for i in range(65, 91):
#         tmp.append(chr(i))
#     return tmp
#
# print(abc()[1])
# print(abc()[12])
# print(abc()[22])


"""               """
"""   Function 3  """
"""               """

# def add(number1, number2):
#     print(f"{number1} + {number2} = {number1 + number2}")
#
#
# add(20, 30)


"""               """
"""   Function 4  """
"""               """

# def age(name,year):
#     print(f"{name} {2024-year} years old")
# age("Azizdoni", 2007)


"""               """
"""   Function 5  """
"""               """

# def pow(num1, num2):
#     print(num1 ** num2)
#
#
# pow(9, 2)


"""               """
"""   Function 6  """
"""               """

# def check_num(num1):
#     if num1 % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
#
#
# print(check_num(45))


"""               """
"""   Function 7  """
"""               """

# def check_num(num1):
#     res = ""
#     if num1 > 0:
#         res = "Positive"
#     elif num1 < 0:
#         res = "Negative"
#     else:
#         res = "Zero"
#     return res
#
#
# print(check_num(0))


"""               """
"""   Function 8  """
"""               """


def add(num1: int, num2: int):
    """
    this function add both values of num1 and num2
    :param num1: first number
    :param num2: second number
    :return: result
    """
    return num1 + num2


def substract(num1: int, num2: int):
    """
    this function substract both values of num1 and num2
    :param num1: first number
    :param num2: second number
    :return: result
    """
    return num1 - num2


def multiply(num1: int, num2: int):
    """
    this function multiply both values of num1 and num2
    :param num1: first number
    :param num2: second number
    :return: result
    """
    return num1 * num2


def divide(num1: int, num2: int):
    """
    this function divide both values of num1 and num2
    :param num1: first number
    :param num2: second number
    :return: result
    """
    return num1 / num2
