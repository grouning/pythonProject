# 1. Задача
# a = 35
# b = 48
# c = 'qwerty'
# print(a)
# print(b)
# print(c)

# name = input('Введите имя: ')
# age = input('Введите возраст: ')
# print(name)
# print(age)
# print('Name: ' + name , 'Age: ' + age)

# 2. Задача
# user = int(input('Введите время в секундах: '))
# hours = user // 3600
# minutes = (user - (hours * 3600)) // 60
# seconds = (user - (minutes * 3600)) % 60
# print(f'{hours:02}:{minutes:02}:{seconds:02}')

# 3. Задача
# user = input('Введите число: ')
# res1 = user
# res2 = user * 2
# res3 = user * 3
# last_res = int(res1) + int(res2) + int(res3)
# print(f'{last_res} = {int(res1)} + {int(res2)} + {int(res3)}')

# 4. Задача
# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
# user = int(input('Введите целое положительное число: '))
# max = user % 10
# while user >= 1:
#     user = user // 10
#     if user % 10 > max:
#       max = user % 10
#     if user > 9:
#         continue
#     else:
#         print("Максимальное цифра в числе: ", max)
#         break

# 5. Задача
# gain = int(input('Введите значение выручки: '))
# cost = int(input('Введите значение издержек: '))
# # if gain > cost:
# #     print('Фирма приносит прибыль')
# # else:
# #     print('Фирма работает в убыток')

# 6. Задача
# gain = int(input('Введите значение выручки: '))
# cost = int(input('Введите значение издержек: '))
# if gain > cost:
#     print(f'Рентабельность выручки составляет: {gain / cost:.2f}%')
#     workers = int(input('Введите количество сотрудников: '))
#     print(f'Прибыль на одного сотрудника составляет: {gain / workers:.2f}%')
# else:
#     print('Фирма работает в убыток, пора сокращать')