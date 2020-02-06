seconds = int(input('Введите секунды: '))
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print(f'{hours}:{minutes}:{seconds}')
