def ciphering(word: str, key: int):
    t = ''
    for i in word:
        t += chr(ord(i) + key)
    return t

print(ciphering('salom', 2))
