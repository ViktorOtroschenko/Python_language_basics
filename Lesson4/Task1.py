# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

def salary(production, time, prize):
    money = (production * time) + prize
    return money

try:
    production = float(input('Введите отработанные часы: '))
    time = float(input('Введите ставку в часах: '))
    prize = float(input('Премия:'))
except ValueError:
    print('Попробуйте еще раз!')
else:
    print(f'Размер заработной платы составил: {salary(production, time, prize)}')