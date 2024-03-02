


a = int(input(">>> "))
print(oct(a))
b = ''
while 1 < a:
    b += str(a % 8)
    a = a // 8
b += str(a)
b = "0o" + b[::-1]
print(b)


# a = int(input(">>> "))
# print(hex(a))
# b = ''
# while 1 < a:
#     b += str(a % 16)
#     a = a // 16
# b += str(a)
# b = "0x" + b[::-1]
# if b == 10:
#     b == "a"
# elif b == 11:
#     b == "b"
# print(b)
