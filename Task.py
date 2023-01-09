# Задача 1
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [2, 3, 5, 9, 3]
# sum = 0  

# for i in range(len(list)):
#     if i % 2 != 0:
#         sum += list[i]
    
# print(f'Сумма элементов списка {list} стоящих на нечётной позиции = {sum}')


# Задача 2
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

# list = [2, 3, 4, 5, 6]
# mult_list = []
# i  = 0

# while i < len(list) / 2:
#     mult_list.append(list[i] * list[(len(list)-1)-i])
#     i += 1

# print(f'Произведение пар чисел списка {list} = {mult_list}')


# Задача 3
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [1.1, 1.2, 3.1, 5, 10.01]

# new_list = [round(i % 1, 2) for i in list if i % 1 != 0]
# print(f'Разница между max и min значением дробной части элементов = {max(new_list) - min(new_list)}')


# Задача 4
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример: 45 -> 101101 3 -> 11 2 -> 10

# number = int(input('Введите десятичное число: '))
# s = ''

# while number != 0:
#     s = str(number % 2) + s
#     number //= 2

# print(f'Двоичное число -> {s}')


# Задача 5
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число k: '))

F1 = [0]
item = 1

for i in range(1, k + 1):
    F1.append(item)
    item = F1[i] + F1[i - 1]

F2 = []

for i in range(1, len(F1)):
    F2.insert(0, (-1) ** (i + 1) * F1[i])
    
print(f'Для k = {k} список: {F2 + F1}')
