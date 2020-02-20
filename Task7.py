# Task7.
"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста."""

import json
firm_profit = {}
profit_average = {}
average = 0
i = 0
with open('firms.txt') as f:
    for el in f:
        name, form, income, costs = el.split()
        firm_profit[name] = int(income) - int(costs)
        if firm_profit.setdefault(name) > 0:
            average = average + firm_profit.setdefault(name)
            i += 1
    if i != 0:
        prof_average = average / i
    profit_average = {'Средняя прибыль': int(prof_average)}
    firm_profit.update(profit_average)
    print(firm_profit)

with open('firm.json', 'w') as f:
    json.dump(firm_profit, f)
