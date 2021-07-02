# 6. Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import cycle

my_list = [1, 4, 'hi', False, 11, 'word', 4.1, True, None]
print('Сейчас будет бесконечный итератор: продолжить?')
answer = input(f'Y/Q: ')
if answer == 'Y' or answer == 'y':
    for el in cycle(my_list):
        print(el)
elif answer == 'Q' or answer == 'q':
    print('Может, ещё раз?')
else:
    print('Неизвестный ответ!')

