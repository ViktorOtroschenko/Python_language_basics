name = input('Введите ваше имя: ').title()
surname = input('Введите вашу фамилию: ').title()
date = input('Введите вашу дату рождения: ')
city = input('Введите ваш город: ').title()
email = input('Введите ваш email: ')
telephone = input('Введите ваш телефон: ')

def my_history(name, surname, date, city, email, telephone):
    return' '.join([name, surname, date, city, email, telephone])

print(my_history(name, surname, date, city, email, telephone))
