def my_func(*args):
    number1 = int(input('Введите первое число: '))
    number2 = int(input('Введите второе число: '))
    return number1 / number2


try:
    division = my_func()
except ZeroDivisionError:
    print('Деление на ноль!')
print(my_func())
