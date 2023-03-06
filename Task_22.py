# Задача 22: Даны два неупорядоченных набора целых чисел 
# (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, 
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

import random
n = int (input('Количество первого множества  : '))
m = int (input('Количество второго множества  : '))
first_set = {random.randint(1,100) for _ in range(n)}
second_set = {random.randint(1,100) for _ in range(m)}

print('Первый набор чисел: ', first_set)
print('Второй набор чисел: ', second_set)

intersection = list(first_set & second_set)
intersection.sort()
print (f'Числа, встречающиеся в обоих множествах, в порядке возрастания: {intersection}')

