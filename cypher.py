"""

chr = code to letter
ord = letter to code

"""

word = input("word >> ")
key = int(input("key >> "))
t1 = ''

for i in word:
    t1 += chr(ord(i) + key)
print(t1)



