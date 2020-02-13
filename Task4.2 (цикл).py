x = float(input('Введите число: '))
y = float(input('Введите отрицательное число: '))
i = 0
while i <= 0:
    result = x ** y
    i -= 1
    if i == y:
        break
print(result)