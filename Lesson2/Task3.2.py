seasons = ['Зима', 'Весна', 'Лето', 'Осень']

month = int(input('Введите месяц года числом: '))
if month == 1 or month == 2 or month == 12:
    print('Этот месяц:', seasons[0])
elif month == 3 or month == 4 or month == 5:
    print('Этот месяц:', seasons[1])
elif month == 6 or month == 7 or month == 8:
    print('Этот месяц:', seasons[2])
elif month == 9 or month == 10 or month == 11:
    print('Этот месяц:', seasons[3])
else:
    print('В году 12 месяцев!')
