# un_id = {
#     932608005: 1243123,
#     938005493: 4356872,
#     994699007: 5476689
# }
#
# data = {
#     1243123: {
#         'name': 'Azizbek',
#         "surname": 'Rahimjonov',
#         'pass': 'Ab7648967',
#         'date': '17.04.2015'},
#     938005493: {
#         'name': 'Azizbek',
#         "surname": 'Doniyorov',
#         'pass': 'AB9319344',
#         'date': '07.07.2017'},
#     5476689: {
#         'name': 'MuhammadAli',
#         "surname": 'Rustamov',
#         'pass': 'AB4325141',
#         'date': '08.07.2019'
#     }}
#
# msg_pn = int(input('Enter PhoneNumber: '))
# userID = un_id.get(msg_pn)
#
# if userID is not None:
#     print(userID)
#     msg_id = int(input('Enter user ID: '))
#
#     b = data.get(msg_id)
#     if b is not None:
#         print(b)
#     else:
#         print("you are freak")
# else:
#     print("you are freak")
