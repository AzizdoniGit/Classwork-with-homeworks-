input_number = int(input("Enter an integer: "))


print(hex(input_number))


hex_value = ""
while input_number > 0:
    digit = input_number % 16
    if digit < 10:
        hex_value = str(digit) + hex_value
    else:
        hex_value = chr(ord('A') + digit - 10) + hex_value
    input_number //= 16

print(f"The hex is 0x{hex_value}")
