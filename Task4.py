line = input('Введите предложение: ')
word = []
number = 1
for el in range(line.count(' ') + 1):
    word = line.split()
    if len(str(word)) <= 10:
        print(f' {number} {word [el]}')
        number = number + 1
    else:
        print(f' {number} {word [el] [0:10]}')
        number = number + 1
