# n = int(input("Enter a number: "))
#
# if n > 0:
#     n = n + 1
#
# print(n)

""" Second if"""

# n = int(input("Enter a number: "))
#
# if n > 0:
#     n = n + 1
# else:
#     n = n - 2
#
# print(n)


""" Third if """

n = int(input("Enter a number: "))

if n > 0:
    n = n + 1
elif n < 0:
    n = n - 2
else:
    n = 10

print(n)


""" Fourth If """

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

count = 0

if a > 0:
    count = count + 1

if b > 0:
    count = count + 1

if c > 0:
    count = count + 1

print(count)

""" Fifth if"""

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

pos = 0
neg = 0

if a > 0:
    pos = pos + 1
elif a < 0:
    neg = neg + 1

if b > 0:
    pos = pos + 1
elif b < 0:
    neg = neg + 1

if c > 0:
    pos = pos + 1
elif c < 0:
    neg = neg + 1

print("Positive:", pos)
print("Negative:", neg)


""" Sixth if"""

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print(a)
else:
    print(b)


""" Seventh if """

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a < b:
    print(1)
else:
    print(2)


""" Eighth if"""

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a > b:
    print(a, b)
else:
    print(b, a)


""" Nineth if """

A = float(input("Enter the first number: "))
B = float(input("Enter the second number: "))

if A > B:
    A, B = B, A

print(A, B)



""" Tenth If"""

A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))

if A != B:
    A = A + B
    B = A
else:
    A = 0
    B = 0

print(A, B)