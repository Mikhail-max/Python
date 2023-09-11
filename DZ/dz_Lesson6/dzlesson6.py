# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# def list1(a1,d,n):
#     for i in range(n):
#         print(a1 + i * d, end='\n')


# a1= int(input("Введите первый элемент: "))
# d= int(input("Введите разность элементов в прогрессии: "))
# n= int(input("Введите количество элементов: "))
# list1(a1,d,n)


# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]
import random

def index(list, diapazon_min, diapazon_max):
    result = []
    for i in range(len(list)):
        if list[i] >= diapazon_min and list[i] <= diapazon_max:
            result.append(i)
    return print(result)

dlist_min = int(input("Введите минимальный диапазон случайных чисел в списке: "))
dlist_max = int(input("Введите максимальный диапазон случайных чисел в списке: "))
diapazon_min = int(input("введите минимальный диапазон поиска: "))
diapazon_max = int(input("Введите максимальный диапазон поиска: "))
list_lenght = int(input("Введите длину списка: "))
list1 = [random.randint(dlist_min,dlist_max) for i in range(list_lenght)]
print(list1)
index(list1, diapazon_min, diapazon_max)