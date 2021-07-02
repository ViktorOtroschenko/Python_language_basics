# Task4.
"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

word = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
rus_word = []
with open('numbers.txt', 'r') as f_1:
    for el in f_1:
        el = el.split(' ', 1)
        rus_word.append(word[el[0]] + ' ' + el[1])
    print(rus_word)

with open('new_numbers.txt', 'w') as f_2:
    f_2.writelines(rus_word)
