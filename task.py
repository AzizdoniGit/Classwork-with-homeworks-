# import pyttsx3
#
# one_unit = {
#     '0': "zero",
#     '1': "one",
#     '2': "two",
#     '3': "three",
#     '4': "four",
#     '5': "five",
#     '6': "six",
#     '7': "seven",
#     '8': "eight",
#     '9': "nine",
# }
#
# two_unit = {
#     '1': "ten",
#     '2': "twenty",
#     '3': "thirty",
#     '4': "forty",
#     '5': "fifty",
#     '6': "sixty",
#     '7': "seventy",
#     '8': "eighty",
#     '9': "ninety",
# }
#
#
# for i in range(50, 100, 10):
#     print(i)
#     ask = i
#
#
#     result1 = ask // 10
#     result2 = ask % 10
#
#     word_to_speak = ""
#
#     if ask == 11:
#         word_to_speak = "eleven"
#     elif ask == 12:
#         word_to_speak = "twelve"
#     elif ask == 13:
#         word_to_speak = "thirteen"
#     elif ask == 14:
#         word_to_speak = "fourteen"
#     elif ask == 15:
#         word_to_speak = "fifteen"
#     elif ask == 16:
#         word_to_speak = "sixteen"
#     elif ask == 17:
#         word_to_speak = "seventeen"
#     elif ask == 18:
#         word_to_speak = "eighteen"
#     elif ask == 19:
#         word_to_speak = "nineteen"
#     elif result1 > 0:
#         if two_unit.get(str(result1)) is None or one_unit.get(str(result2)) is None:
#             word_to_speak = "Your number equals to three units or more"
#         else:
#             word_to_speak = f"{two_unit.get(str(result1))}"
#             if result2 > 0:
#                 word_to_speak += f" {one_unit.get(str(result2))}"
#     else:
#         if one_unit.get(str(result2)) is None:
#             word_to_speak = "Your number equals to three units or more"
#         else:
#             if result2 > 0:
#                 word_to_speak = f"{one_unit.get(str(result2))}"
#
#
#     engine = pyttsx3.init()
#
#
#     en_voice_id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
#     engine.setProperty('rate', 150)
#     engine.setProperty('voice', en_voice_id)
#     print(word_to_speak)
#     engine.say(f"{word_to_speak}")
#     engine.runAndWait()
#
