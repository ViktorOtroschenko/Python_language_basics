money = int(input('Введите прибыль фирмы за месяц: '))
costs = int(input('Введите издержки фирмы за месяц: '))
if money >= costs:
    print('За прошедший месяц фирма получила прибыль!')
    profitability = money / costs
    print('Рентабельность выручки составила:', profitability)
    staff = int(input('Введите количество сотрудников фирмы: '))
    profit = int((money - costs) / staff)
    print('Прибыль на каждого сотрудника составила:', profit)
elif money <= costs:
    print('За прошедший месяц только расходы! Нужно больше работать!')
