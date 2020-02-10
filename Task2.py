print('Давайте создадим список!')
element_1 = input('Введите число: ')
element_2 = input('Введите число: ')
element_3 = input('Введите число: ')
element_4 = input('Введите число: ')
element_5 = input('Введите число: ')

my_list = [element_1, element_2, element_3, element_4, element_5]

print(my_list)
answer = input('Поменяем местами элементы списка? Да/Нет?')

if answer == 'Да' or answer == 'да':
    my_list[0], my_list[1] = my_list[1], my_list[0]
    my_list[2], my_list[3] = my_list[3], my_list[2]
elif answer == 'Нет' or answer == 'нет':
    print('Очень жаль!')
else:
    print('Неизвестный ответ!')
print(my_list)