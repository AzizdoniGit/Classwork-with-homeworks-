import random

word = random.choice(
    ["Lamborghini", "Porsche", "RolceRoys", "RangeRover", "Bugatti", "Ferrari", "WolksVagen", "Audi", "Chevrolet", "Pagani", ])
hide_word = list('_' * len(word))
chance = int(len(word) * 1.5)
i = 0
print(f"You have {chance} chances. Please choose using your brain not stupidity 😊")

while i < chance:
    if hide_word == list(word):
        print('You won 2000$ !🥳')
        print(''.join(hide_word))
        break
    print(''.join(hide_word))
    message = input('Enter letter: ')[0]  # a
    if message in word:
        ind_word = 0
        while ind_word < len(word):
            if word[ind_word] == message:
                hide_word[ind_word] = message
            ind_word += 1
        print("Good job 👌")

    i += 1
    print(f"You have {i} chances. Please be patient and smart 😊")
