product = int(input('Введите количество товара: '))
my_catalog = []
my_analysis = {'Наименование': [], 'Цена': [], 'Количество': [], 'ЕД': []}
my_dict = []
number = 1
while number <= product:
    my_catalog = dict({'Наименование': input('Введите название товара: '), 'Цена': int(input('Введите цену: ')),
                       'Количество': int(input('Введите необходимое количество: ')),
                       'Ед': input('Введите единицу измерения:')})
    my_dict.append((number, my_catalog))
    number += 1
    my_analysis = dict({'Наименование:': [my_catalog.get('Наименование')], 'Цена:': [my_catalog.get('Цена')],
                       'Количество:': [my_catalog.get('Количество')], 'Ед': [my_catalog.get('Ед')]})

print(f'\n Список товара:')
for key, value in my_dict:
    print(f'{key}: {value}')

print(f'\n Анализ товара:')
for key, value in my_analysis.items():
    print(f'{key}: {value}')
