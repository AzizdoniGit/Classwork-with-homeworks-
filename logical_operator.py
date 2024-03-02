""""""
# AND = True and False == False
""""""

# n = int(input(">> "))
# a =  n > 20 and n < 30
# if a:
#     print("GO")
# else:
#     print("Leave now bastard!")

""""""
# OR = True and False == True
""""""

# n = input(">> ").lower()
# a =  n == "passport" or n == "idcard"
# if a:
#     print("GO")
# else:
#     print("Leave bastard !")

""""""
# NOT = True == False
""""""

# n = not (True)
# print(n)


""""""
# IN = if it was existed True
""""""

# data = "uzbTiger, uzbWolf, Default, Revolution, InvEvolution"
# nickname = input(">> ")
#
# if nickname in data:
#     print("This username has already taken")
# else:
#     print("Your username successfully put")


""""""
# not in = if it wasn't existed True
""""""

# data = "uzbTiger, uzbWolf, Default, Revolution, InvEvolution"
# nickname = input(">> ")
#
# if nickname not in data:
#     print("Your username successfully put")
# else:
#     print("This username has already taken")


""""""
# is = the same function as ==
""""""

# b = type("13") is str
# print(b)

a = int(input(">> "))
if type(a) is str:
    print("It is in type of string")
if type(a) is int:
    a**2
    print(a)
if a is float:
    a // 2
