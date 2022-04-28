# 1. Задача.
# li = [1234, 'ffgs', 2423.123, False, '@&$(*($~']
# for i in li:
#     print(type(i))

# 2. Задача.
# el_count = int(input("Введите количество элементов списка "))
# my_list = []
# i = 0
# el = 0
# while i < el_count:
#     my_list.append(input("Введите следующее значение списка "))
#     i += 1
#
# for elem in range(int(len(my_list)/2)):
#         my_list[el], my_list[el + 1] = my_list [el + 1], my_list[el]
#         el += 2
# print(my_list)

# 3. Задача.
# seasons_list = ['winter', 'spring', 'summer', 'autumn']
# seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
# month = int(input("Введите месяц по номеру от 1 до 12: "))
# if month ==1 or month == 12 or month == 2:
#         print(seasons_dict.get(1))
#         print(seasons_list[0])
# elif month == 3 or month == 4 or month ==5:
#     print(seasons_dict.get(2))
#     print(seasons_list[1])
# elif month == 6 or month == 7 or month == 8:
#     print(seasons_dict.get(3))
#     print(seasons_list[2])
#
# elif month == 9 or month == 10 or month == 11:
#     print(seasons_dict.get(4))
#     print(seasons_list[3])
# else:
#         print("Такого месяца не существует")

# 4. Задача.
# my_str = input("Введите строку из нескольких слов разделённых пробелами: ")
# a = my_str.split(' ')
# for i, el in enumerate(a, 1):
#     if len(el) > 10:
#         el = el[0:10]
#     print(f"{i}. - {el}")

#5. Задача.
# number = int(input("Введите элемент рейтинга: "))
# my_list = [7, 4, 3, 2]
# c = my_list.count(number)
# for element in my_list:
#     if c > 0:
#         i = my_list.index(number)
#         my_list.insert(i+c, number)
#         break
#     else:
#         if number > element:
#             j = my_list.index(element)
#             my_list.insert(j, number)
#             break
#         elif number < my_list[len(my_list) - 1]:
#             my_list.append(number)
# print(my_list)