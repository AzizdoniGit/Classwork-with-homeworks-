# def addition(n):
#     return n + n
#
#
# numbers = (1, 2, 3, 4)
# result = map(addition, numbers)
# print(list(result))


# def up(a:str):
#     return a.upper()
# fruits = ["apple", "banana", "mango", "pineapple"]
# new_fruits = []
# for i in range:
#     new_fruits.append(up(i))
# print(new_fruits)


""" making it shorter by using map function (clean code)"""

# fruits = ["apple", "banana", "mango", "pineapple"]
# new_fruits = list(map(lambda a: a.upper(), fruits))
# print(new_fruits)


""" Challenge 1 """

# fruits = ["apple", "banana", "mango", "pineapple"]
# new_fruits = list(map(lambda a: len(a), fruits))
# print(new_fruits)

""" Challenge 2 """

# numbers_pow = list(map(lambda i: i**2, list(range(1, 100))))
# print(numbers_pow)

""" Challenge 3 """

# a = list(range(1, 100))
# is_even_pow = list(map(lambda i: i**2 if i%2==0 else "", a))
# print(is_even_pow)


""" Challenge 4 """


# def ciphering(word: str):
#     ciphered_text = ''
#     for i in word:
#         ciphered_text += chr(ord(i) + 2)
#     return ciphered_text
#
#
# text_for_ciphering = ["salom", "freak", "donik121321", "hello12431234", "qwerty12323498312514123987"]
# ciphering_map = list(map(ciphering, text_for_ciphering))
# print(ciphering_map)





