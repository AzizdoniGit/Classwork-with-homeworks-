import random

"""

randint = int random
uniform - float random

"""

# number = []
# stop = "938005493"
# i = 0
#
# while i < 100:
#     if number == 938005493:
#         print("exist")
#         break
#     else:
#         number = random.randint(100000000, 999999999)
#         print(f"+998{number}")
#         i += 1
#         print(i)


correct_answer = 0
wrong_answer = 0

while True:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    question = int(input(f"{a} + {b}: "))
    if question == a + b:
        print("Good job")
        correct_answer += 1
    else:
        print("Maybe, u did smth wrong. Try again 😊")
        wrong_answer += 1
        if wrong_answer == 5:
            if correct_answer > 30:
                print("Your mark is '5'")
            elif 29 >= correct_answer >= 20:
                print("Your mark is '4'")
            elif 19 >= correct_answer >= 10:
                print("Your mark is '3'")
            elif 9 >= correct_answer >= 0:
                print("Your mark is '2'")
            print(f"Your correct answers: {correct_answer}, Your incorrect answers: {wrong_answer}")
            break
        continue
