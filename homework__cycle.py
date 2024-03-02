""""""""
""" Task 1 """
""""""""

# my_list = [5, 2, 9, 7, 1, 4, 6, 8, 3]
#
# for i in range(len(my_list) - 1):
#     for j in range(i + 1, len(my_list)):
#         if my_list[i] > my_list[j]:
#             sort = my_list[i]
#             my_list[i] = my_list[j]
#             my_list[j] = sort
#
# print(my_list)


""""""""
""" Task 2 """
""""""""


my_list = [1, 2, 3, 4, 5]

reversed_list = []

for i in range(len(my_list) - 1, -1, -1):
    reversed_list.append(my_list[i])

print(reversed_list)
