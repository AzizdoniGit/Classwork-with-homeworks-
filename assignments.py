""" Integer 1 """

# cm = int(input("Write cm here: "))
# meter = cm / 100
# print(meter)


""" Integer 2 """

# kg = int(input("Write kg here: "))
# ton = kg / 1000
# print(ton)


""" Integer 3 """

# byte = int( input( "Write bytes here: " ) )
# kbyte = byte / 1024
# print( kbyte )


""" Integer 4 """

# A = int( input( "Write the first value: " ) )
# B = int( input( "Write the second value: " ) )
# result = A // B
# print( result )

""" Integer 5 """

# A = int( input( "Write the first value: " ) )
# B = int( input( "Write the second value: " ) )
# result1 = A // B
# result2 = A%B
# print( result1, result2 )


""" Integer 6 """

# a = int( input( "Write the number which is contains two value: Example: 45,23,14. Write here: " ) )
# twoNumber = a // 10
# oneNumber = a%10
# print(twoNumber, oneNumber)


""" Integer 7 """

# a = int( input( "Write the number which is contains two value: Example: 45,23,14. Write here: " ) )
# twoNumber = a // 10
# oneNumber = a%10
# print(twoNumber, oneNumber)


""" Integer 8 """

# a = int(input("Write the number which is contains two value: Example: 45,23,14. Write here: "))
# b = int(input("Write the number which is contains two value: Example: 45,23,14. Write here: "))
# a, b = b, a
# print(a, b)

""" Integer 9 """

# a = int(input("Write the number which is contains three value: Example: 454,232,141. Write here: "))
# hundreds = a // 100
# print(hundreds)


""" Integer 10 """

# a = int(input("Write the number which is contains three value: Example: 454,232,141. Write here: "))
# units = a % 10
# tens = (a // 10) % 10
# print(units, tens)

""" Integer 11 """

# a = int(input("Write the number which is contains three value: Example: 454,232,141. Write here: "))
# hundreds = (a // 100) % 10
# tens = (a // 10) % 10
# units = a % 10
# print(units + tens + hundreds)


""" Integer 12 """

# a = int(input("Write the number which is contains three value: Example: 454,232,141. Write here: "))
# hundreds = (a // 100) % 10
# tens = (a // 10) % 10
# units = a % 10
# print(f"{units}{tens}{hundreds}")


""" Integer 13 """

# a = int(input("Write the number which is contains three value: Example: 454,232,141. Write here: "))
# first = a // 100
# rest = a % 100
# result = rest * 10 + first
# print(result)


""" Integer 14 """

# a = int(input("Write the number which is contains three value: Example: 454,232,141. Write here: "))
# last = a % 10
# rest = a // 10
# result = last * 100 + rest
# print(result)

""" Integer 15 """

# a = int(input("Write the number which is contains three value: Example: 454,232,141. Write here: "))
# hundreds = a // 100
# tens = (a // 10) % 10
# units = a % 10
# result = tens * 100 + hundreds * 10 + units
# print(result)


""" Integer 16 """

# a = int(input("Write the number which is contains three value: Example: 454,232,141. Write here: "))
# hundreds = a // 100
# tens = (a // 10) % 10
# units = a % 10
# result = hundreds * 100 + units * 10 + tens
# print(result)


""" Integer 17 """

# a = int(input("Write the number which is contains more than three value: Example: 999, 1000, 1130 . Write here: "))
# hundreds = (a // 100) % 10
# print(hundreds)


""" Integer 18 """

# a = int(input("Write the number which is contains more than three value: Example: 999, 1000, 1130 . Write here: "))
# thousands = a // 1000
# print(thousands)


""" Integer 19 """

# seconds = int(input("Write seconds: "))
# minutes = seconds // 60
# print(minutes)


""" Integer 20 """

seconds = int(input("Write seconds: "))
hours = seconds // 3600
print(hours)
