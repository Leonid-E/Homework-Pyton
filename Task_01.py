# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается 
# в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, 
# максимально близкое ему по значению

import random
length = int (input('Длина массива : '))
my_list = [random.randint(1,100) for _ in range(length)]
print (my_list)
x = int (input('Искомое число "х" : '))
coincidences = 0 
close_values = 0
for i in my_list:
    if i == x:
        coincidences += 1 
    if (i == (x + 1) or i == (x + 2)) or (i == (x - 1) or i == (x - 2)):
        close_values += 1
print('Повторяется ', coincidences, ' раз')
print('Близкие по значению числа (',x, '± 2) повторяются ', close_values, ' раз')
        
