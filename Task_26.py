# Задача 26:  
# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B 
# с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

number = int(input("Введите число: "))
multi = int(input("Введите степень: "))

def degree(number, multi):
    if multi == 1:
        return (number)
    else:
        return (number * degree(number, multi - 1))

result = degree(number, multi)
print(f'{number} в {multi}-й степени = {result}')