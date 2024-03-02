def filter_int(place):
    if type(place) is int:
        return True
    elif type(place) is str:
        return False

word = ["apple", 4, 2, "challenge", 3]

res = list(filter(filter_int, word))
print(res)



def filter_str(place):
    if type(place) is str:
        return True
    elif type(place) is int:
        return False

word = ["apple", 4, 2, "challenge", 3]

res = list(filter(filter_str, word))
print(res)
