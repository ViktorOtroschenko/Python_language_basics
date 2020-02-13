score = True
sum_result = 0
while score == True:
    numbers = input('Для выхода нажмите Q!\n'
                    'Введите строку чисел, через пробел:').split(' ')
    result = 0
    for el in numbers:
        if el == 'q' or el == 'Q':
            score = False
            break
        else:
            result = result + int(el)
    sum_result = sum_result + result
    print(f'Ваша сумма:{sum_result}')

print(f'Финальная сумма: {sum_result}')
