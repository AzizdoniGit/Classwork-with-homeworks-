'''W1'''

# a = int(input("Write a year: "))
#
# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print("29 February")
# else:
#     print("28 February")


'''W2'''

# user1 = int(input("number one: "))
# user2 = int(input("number two: "))
# user3 = int(input("number three: "))
# myNum1 = 5
# myNum2 = 2
# myNum3 = 3
#
# Strike = 0
# Bool = 0
#
# if user1 == myNum1:
#     Strike += 1
# else:
#     Bool += 1
#
# if user2 == myNum2:
#     Strike += 1
# else:
#     Bool += 1
#
# if user3 == myNum3:
#     Strike += 1
# else:
#     Bool += 1
#
# print("\nStrike equals to:", Strike)
# print("Bool equals to:", Bool)

'''W3'''

# temperature = int(input("Write the temperature of outdoor: "))
#
# if temperature <= 40 and temperature >= 0:
#     print("You can leave your home")
# else:
#     print("Stay at home !")


"""Guess game"""

# muNumber = 7
#
# option1 = int(input("Choose first number between 1 to 10: "))
#
# if option1 > muNumber and option1 > 0:
#     print("Go down")
# elif option1 < muNumber and option1 > 0:
#     print("Go up")
# elif option1 == muNumber:
#     print("You found my number", )
#
# option2 = int(input("Choose second number between 1 to 10: "))
#
# if option2 > muNumber and option2 > 0:
#     print("Go down")
# elif option2 < muNumber and option2 > 0:
#     print("Go up")
# elif option2 == muNumber:
#     print("You found my number", )
#
# option3 = int(input("Choose third number between 1 to 10: "))
#
# if option3 > muNumber and option3 > 0:
#     print("Go down")
# elif option3 < muNumber and option3 > 0:
#     print("Go up")
# elif option3 == muNumber:
#     print("You found my number", )
#
# if option1 and option2 and option3 != muNumber:
#     print("\t Don't be a looser")


number = input("Write letter: ")
ords = ord(number)
print(ords)

if ords and number != "1" and "2" and "3" and "4" and "5" and "6" and "7" and "8" and "9":
   print(chr(ords + 32))


#
# print(ord('A'))
# print(chr(65))

