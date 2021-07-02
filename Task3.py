number1 = int(input('Введите первый аргумент: '))
number2 = int(input('Введите второй аргумент: '))
number3 = int(input('Введите третий аргумент: '))

def my_func(number1, number2, number3):
    if number1 > number3 and number2 > number3:
        return number1 + number2
    elif number1 > number2 and number2 < number3:
        return number1 + number3
    else:
        return number2 + number3

print(f'Сумма двух наибольших аргументов: {my_func(number1, number2, number3)}')


