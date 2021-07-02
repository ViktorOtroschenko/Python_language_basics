# Task2.
"""Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""

f = open('123.txt', 'r')
print('Количество строк в файле: {}'.format(len(f.readlines())))

f = open('123.txt', 'r')
lines = f.readlines()
for el in range(len(lines)):
    print(f'Количество слов в {el + 1} строке: {len(lines[el].split())}')
f.close()
