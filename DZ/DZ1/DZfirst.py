# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
number = input("Введите трехзначное число: ")
print(f"Сумма чисел трехзначного числа равна: {int(number[0]) + int(number[1]) + int(number[2])}")