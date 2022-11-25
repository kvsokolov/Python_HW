# # Part 1 11/25/2022
# # Konstantin Sokolov

import random

# FUNCTIONS

def inputFloatNumber(sourceText):
    isAccepted = False
    while not isAccepted:
        try:
            number = float(input(f'{sourceText}'))
            isAccepted = True
        except ValueError:
            print('Это не число!')
    return number

def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


def factorialSequence(n):
    lst = []
    for i in range(1, n + 1):
        lst.append(fact(i))
    return lst

def myShuffle(lst):
    for i in range(len(lst)):
        tmp = lst[i]
        temp = random.randrange(len(lst))
        lst[i] = lst[temp]
        lst[temp] = tmp
    return lst


# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

print('1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.\n')

num1 = input('Введите число: ')
temp = 0
for i in num1:
    if i != '.':
        temp += int(i)
print(f'Сумма цифр = {temp}!')

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

print('\n2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.\n')

num2 = int(inputFloatNumber('Введите число: '))
print(f'Последовательность: {factorialSequence(num2)}')

# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

print('\n3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.\n')

num3 = int(inputFloatNumber('Введите число: '))
tmp = 0
for i in range(1, num3 + 1):
    tmp += (1+1/i)**i
print(f'Сумма = {round(tmp, 2)}!')

# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3]
# --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

print('\n4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].\nНайдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.\n')

num4 = int(inputFloatNumber('Введите n: '))
list4 = []
for i in range(-num4, num4 + 1):
    list4.append(i)
print(list4)
tmpList4 = list(map(int, input('--> ').split()))
result = 1
for i in tmpList4:
    result *= list4[i]
print(f'Вывод: {result}')

# 5. Реализуйте алгоритм перемешивания списка.

print('\n5. Реализуйте алгоритм перемешивания списка.\n')

list5 = []
for i in range(1, 40):
    list5.append(random.randrange(100))
print(list5)
list5 = myShuffle(list5)
print(list5)

