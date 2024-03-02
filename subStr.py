# a = "Assalomu Aleykum"
# print(a[0])


# Task 1

inputName = input(">> ")
FirstName = inputName.index(" ")
print(inputName[0:FirstName])


# Task

inputName = input(">> ")
FirstName = inputName.index(" ")
LastName = inputName.index(" ")
Name = inputName[0:FirstName]
Surname= inputName[LastName+1:]
print(Name[0]+".", Surname[0]+".")