input_number = int(input("Enter an integer: "))
result = ""

while input_number > 0:
    a = input_number % 8
    result = str(a) + result
    input_number = input_number // 8

print(f"The oct is 0o{result}")

print(oct(12))