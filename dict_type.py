# dict()  - dictionary

# b = {
#     'brend': "nike",
#     'model': "air jordan",
#     'price': 200
# }
#
# a = input(">> ")
# print(b.get(a))

# eng = {
#     'greeting': 'Hello',
#     'vehicle': 'car'
# }
#
# uzb = {
#     'greeting': 'Salam',
#     'vehicle': 'moshina'
# }
#
# user = uzb.get(input(">> "))
# print(user)


# data = {
#     'brend': "BMW",
#     'model': "M5",
#     'price': 50
# }
#
# a = input(">> ")
# print(data.get(a))


# a= [1,2,4 [5,6,7,[8,9,10]]]
# b = a[3][3][1]
# print(b)


# update usage one
# data = {
#     'brend': "BMW",
#     'model': "M5",
#     'price': 50
# }
#
# data['price'] = 300
# print(data)

# update usage two
# data = {
#     'brend': "BMW",
#     'model': "M5",
#     'price': 50
# }
#
# data.update({'price': 300})
# print(data)


# data = {
#     'brend': "BMW",
#     'model': "M5",
#     'price': 50
# }

# add new item

# data.update({'color': 'white'})
# print(data)

# remove item

# data.pop({'color'})
# print(data)


data = {
    'brand': "BMW",
    'model': "M5",
    'price': 50
}

a = input(">> ")
res = data.get(a)
if res is not None:
    print(res)
else:
    print("Error")


# print(data.keys())
# print(data.values())



