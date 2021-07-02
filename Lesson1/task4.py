number = int(input('Введите любое целое положительное число: '))
m = number%10
number = number//10
while number > 0:
    if number%10 > m:
        m = number%10
    number = number//10
print('Самая больгая цифра:', m)
