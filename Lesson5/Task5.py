# Task5.
"""Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

try:
    with open('numbs', 'w+') as f:
        numbers = input('Введите число через пробел: ').split(' ')
        print(numbers)
        f.writelines(numbers)
        print('Сумма введённых чисел: {}'.format(sum(map(int, numbers))))
except IOError:
    print('Ошибка!')
except ValueError:
    print('Введено не число. Ошибка ввода-вывода!')
finally:
    f.close()
