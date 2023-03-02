# Вторая задача:
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную 
# ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков

# Напишите программу, которая вычисляет стоимость 
# введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.

# ноутбук 12
word = input('Введите слово : ').lower() # нижний регистр 
en_point_1 = 'AEIOULNSTR'
en_point_2 = 'DG'
en_point_3 = 'BCMP'
en_point_4 = 'FHVWY'
en_point_5 = 'K'
en_point_8 = 'JX'
en_point_10 = 'QZ'

ru_point_1 = 'АВЕИНОРСТ'
ru_point_2 = 'ДКЛМПУ'
ru_point_3 = 'БГЁЬЯ'
ru_point_4 = 'ЙЫ'
ru_point_5 = 'ЖЗХЦЧ'
ru_point_8 = 'ШЭЮ'
ru_point_10 = 'ФЩЪ'

new_word = list(word) # разделение слова на символы

caunt = 0

from string import ascii_letters as en
if new_word[0] in en:
    for i in new_word:
        for j in en_point_1.lower():
            if i == j:
                caunt += 1
        for j in en_point_2.lower():
            if i == j:
                caunt += 2
        for j in en_point_3.lower():
            if i == j:
                caunt += 3
        for j in en_point_4.lower():
            if i == j:
                caunt += 4
        for j in en_point_5.lower():
            if i == j:
                caunt += 5
        for j in en_point_8.lower():
            if i == j:
                caunt += 8
        for j in en_point_10.lower():
            if i == j:
                caunt += 10
else:
    for i in new_word:
        for j in ru_point_1.lower():
            if i == j:
                caunt += 1
        for j in ru_point_2.lower():
            if i == j:
                caunt += 2
        for j in ru_point_3.lower():
            if i == j:
                caunt += 3
        for j in ru_point_4.lower():
            if i == j:
                caunt += 4
        for j in ru_point_5.lower():
            if i == j:
                caunt += 5
        for j in ru_point_8.lower():
            if i == j:
                caunt += 8
        for j in ru_point_10.lower():
            if i == j:
                caunt += 10

print(f'Стоимость слова {caunt} очков')