""" first homework """


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def primes_only(*args, **kwargs):
    primes = []
    for arg in args:
        if is_prime(arg):
            primes.append(arg)
    for kwarg in kwargs.values():
        if is_prime(kwarg):
            primes.append(kwarg)
    return primes


print(primes_only(3, 5, 13, 12, 15, 16))

""" second homework """


def ciphering(*args, **kwargs):
    result = []
    for word in args:
        key = kwargs.get('key', 0)
        text = ''
        for i in word:
            text += chr(ord(i) + key)
        result.append(text)
    return ' '.join(result)


print(ciphering('salom', 'wishes', 'element', key=2))

" third homework "


def deciphering(*args, **kwargs):
    result = []
    for word in args:
        key = kwargs.get('key', 0)
        text = ''
        for i in word:
            text += chr(ord(i) - key)
        result.append(text)
    return ' '.join(result)


print(deciphering('ucnqo', 'ykujgu', 'gngogpv', key=2))
