# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

my_list = [2, 4, 1, 15, 3, 7, 16, 11, 20, 5, 4, 22, 3, 1, 6, 8, 10]
print(f'Начальный список: {my_list}')
new_list = [el for el in my_list if my_list.count(el) < 2]
print(f'Новый список: {new_list}')