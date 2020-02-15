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