# For1
# k = int(input("Enter the number k: "))
# n = int(input("Enter the number n: "))
# for i in range(n):
#     print(k)

# For2
# a = int(input("Enter the number a: "))
# b = int(input("Enter the number b: "))
# for i in range(a, b+1):
#     print(i)
# print("Count of numbers: ", b - a + 1)

# For3
# a = int(input("Enter the number a: "))
# b = int(input("Enter the number b: "))
# for i in range(b-1, a, -1):
#     print(i)
# print("Count of numbers: ", b - a - 1)

# For4
# price = float(input("Enter the price of 1 kg of candy: "))
# for i in range(1, 11):
#     print(f"Price of {i} kg of candy: {price * i}")

# For5
# price = float(input("Enter the price of 1 kg of candy: "))
# for i in range(1, 11):
#     print(f"Price of {i/10} kg of candy: {price * i/10}")

# For6
# price = float(input("Enter the price of 1 kg of candy: "))
# for i in range(6, 11):
#     print(f"Price of {i/5} kg of candy: {price * i/5}")

# For7
# a = int(input("Enter the number a: "))
# b = int(input("Enter the number b: "))
# sum = 0
# for i in range(a, b+1):
#     sum += i
# print("Sum of numbers: ", sum)

# For8
# a = int(input("Enter the number a: "))
# b = int(input("Enter the number b: "))
# product = 1
# for i in range(a, b+1):
#     product *= i
# print("Product of numbers: ", product)

# For9
# a = int(input("Enter the number a: "))
# b = int(input("Enter the number b: "))
# sum = 0
# for i in range(a, b+1):
#     sum += i**2
# print("Sum of squares: ", sum)

# For10
# n = int(input("Enter the number n: "))
# sum = 0
# for i in range(1, n+1):
#     sum += 1/i
# print("Sum: ", sum)

# For11
# n = int(input("Enter the number n: "))
# sum = 0
# for i in range(n, 2*n+1):
#     sum += i**2
# print("Sum: ", sum)

# For12
# n = int(input("Enter the number n: "))
# product = 1
# for i in range(1, n+1):
#     product *= 1 + i/10
# print("Product: ", product)

# For13
n = int(input("Enter the number n: "))
sum = 0
for i in range(1, n+1):
    if i % 2 == 0:
        sum -= 1 + i/10
    else:
        sum += 1 + i/10
print("Sum: ", sum)
