# number = int(input("Write number: "))
# comparison = number > 0
#
# if comparison:
#     print("Hello")
# else:
#     print("Bye")

""""""""

# a = int(input(">> "))
# if a % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

""""""""

# a = int(input(">> "))
# result = "even" if a % 2 == 0 else "odd"
# print(result)


""""""""
#
# a = int(input(">> "))
# print("even" if a % 2 == 0 else "odd")


"""
 120 >= "Budjet"
 119 <= "Kotrakt"
"""

# score = int(input("Write your score: "))
# print("Budjet" if score >= 120 else "Kontrakt")

# week = int(input("Day of the week >> "))
# if week == 1:
#     print("Monday")
# elif week == 2:
#     print("Tuesday")
# elif week == 3:
#     print("Wednesday")
# elif week == 4:
#     print("Thursday")
# elif week == 5:
#     print("Friday")
# elif week == 6:
#     print("Saturday")
# elif week == 7:
#     print("Sunday")
# else:
#     print("Are you stupid or what ?")


a = int(input(">> "))
if a >= 100 and a < 1000:
    print("Three unit")
elif a >= 10 and a < 100:
    print("Two unit")
elif a >= 0 and a < 10:
    print("One unit")
else:
    print("Error")
