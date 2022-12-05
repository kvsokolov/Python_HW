# Part 4 12/04/2022
# Konstantin Sokolov

import math
import random
import re
from pathlib import Path


# FUNCTIONS

def countDigits(num: int):
    count = 0
    while num < 0.99:
        num /= 0.1
        count += 1
    return count

def isPrime(num: int):
    if num > 11:
        tmp = 12
    else: tmp = num
    for i in range(2, num):
        if num % i == 0:
            return False
            i += 1
    return True

def func2(num: int):
    lst = []
    for i in range(2, num + 1):
        if isPrime(i):
            lst.append(i)
    return lst

def isDifferent(num: int, myLst: list):
    count = 0
    for i in myLst:
        if num == i:
            count += 1
    if count > 1: return False
    else: return True

indexes = {"0": b'\xe2\x81\xb0',
           "1": b'\xc2\xb9',
           "2": b'\xc2\xb2',
           "3": b'\xc2\xb3',
           "4": b'\xe2\x81\xb4',
           "5": b'\xe2\x81\xb5',
           "6": b'\xe2\x81\xb6',
           "7": b'\xe2\x81\xb7',
           "8": b'\xe2\x81\xb8',
           "9": b'\xe2\x81\xb9'
           }

def degree(deg):
    result = ''
    temp = str(deg)
    for char in temp:
        tmp = indexes[char]
        result += tmp.decode('UTF-8')
    return result

def isSymbolInDict(c):
    if c.encode('utf-8') in indexes.values():
        return True

def decodeDegree(deg):
    result = ''
    tempo = deg.encode('UTF-8')
    for key, value in indexes.items():
        if tempo in value:
            result += key
    return result

def func4(k:int, randomLimit: int):
    result = ''
    lst = []
# CREATE RANDOM LIST
    for i in range(0, k + 1):
        lst.append(random.randint(0, randomLimit))
# CHECK WHAT POSITION AND INSERT VALUE IN STRING
    for i in range(0, k + 1):
        if lst[i] > 0:
            isNextPosExists = False
            if i < len(lst) - 2:
                if lst[i] > 1:
                    result += f'{lst[i]}x{degree(k-i)}'
                else: result += f'x{degree(k-i)}'
            if i == len(lst) - 2:
                if lst[i] > 1:
                    result += f'{lst[i]}x'
                else: result += 'x'
            elif i == len(lst) - 1:
                if lst[i] >= 1:
                    result += f'{lst[i]}'
                break
            for pos in range(i + 1, k + 1):
                if lst[pos] > 0:
                    isNextPosExists = True
            if isNextPosExists:
                result += ' + '
# IS THERE AN EMPTY STRING OR NOT
    if len(result) > 0:
        result += ' = 0'
        return result
    else: return 'Empty string'


def strToDict(str):
    str = re.sub(r' = 0', '', str)
    str = str.split(sep = ' + ')
    tDict = {}
    for i in str:
        tKey = ''
        tVal = ''
        if re.search(r'\d$', i) != None:
            tKey = '0'
            tVal = i
            tDict[int(tKey)] = int(tVal)
        elif re.search(r'x$', i):
            tKey = '1'
            if len(i) == 1:
                tVal = '1'
            else:
                tVal = re.sub(r'x', '', i)
            tDict[int(tKey)] = int(tVal)
        elif re.search(r'x\D', i):
            for j in i.split(sep = 'x'):
                if j == '':
                    tVal = '1'
                else: 
                    try:
                        tVal = int(j)
                    except:
                        for k in j:
                            tKey += decodeDegree(k)
            tDict[int(tKey)] = int(tVal)
    return tDict

def printDict(dict):
    for key, value in dict.items():
        print(f'{key} ---> {value}')

def func5(dict):
    result = ''
    for key, value in reversed(sorted(dict.items(), key=lambda x: x[0])):
        if key == 0:
            result += f'{value} = 0'
        elif key == 1 and value != 1:
            result += f'{value}x + '
        elif value == 1 and key != 1:
            result += f'x{degree(key)} + '
        elif value == 1 and key == 1:
            result += f'x + '
        else:
            result += '{}x{} + '.format(value, degree(key))
    return result

# 1. Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14

#     Ввод: 0.001
#     Вывод: 3.141

print('1. Вычислить число c заданной точностью d\n')

num1 = float(input('Ввведите математическую точность: '))
print(round(math.pi, countDigits(num1)))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print('\n2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.\n')

num2 = int(input('Ввведите натуральное число: '))
print(func2(num2))

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

print('\n3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.\n')

myLst = []
for i in range(0, 16):
    myLst.append(random.randint(0, 9))
print(f'Сформированный список: {myLst}')
myLst2 = []
for i in myLst:
    if isDifferent(i, myLst):
        myLst2.append(i)
print(f'Список неповторяющихся элементов исходной последовательности: {myLst2}')

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.

print('\n4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.\n')

str4 = func4(15, 100)
print(str4)
with open('task_4.txt', 'w') as f:
    f.write(str4)
print('Файл task_4.txt сохранен...')

# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов 
#(складываются числа, у которых "х" в одинаковых степенях).

print('\n5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов\n(складываются числа, у которых "х" в одинаковых степенях).\n')

with open('first_file.txt', 'w') as f:
    f.write(f'{func4(15, 5)}')
with open('second_file.txt', 'w') as f:
    f.write(f'{func4(10, 5)}')

try:
    with open('first_file.txt', 'r') as f:
        firstString = f.read()
except FileNotFoundError:
    print('Файл "first_value.txt" не существует')

try:
    with open('second_file.txt', 'r') as f:
        secondString = f.read()
except FileNotFoundError:
    print('Файл "second_file.txt" не существует')

firstDict = strToDict(firstString)

print('Первый многочлен:')
print(firstString)

secondDict = strToDict(secondString)

print('Второй многочлен:')
print(secondString)

resultDict = {}
resultDict.update(firstDict)
resultDict.update(secondDict)

for key in secondDict:
    if key in firstDict:
            resultDict[key] = firstDict[key] + secondDict[key]
    else: pass

resultStr = func5(resultDict)

print('Сумма многочленов:')
print(resultStr)
with open('result_file.txt', 'w') as f:
    f.write(f'{resultStr}')
    print('Файл "result_file.txt" сохранен...')

