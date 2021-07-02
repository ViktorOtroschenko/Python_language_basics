# Task4.
"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
40 (WorkCar) должно выводиться сообщение о превышении скорости. Создайте экземпляры классов, передайте значения
атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат."""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала.')

    def stop(self):
        print(f'Машина {self.name} остановилась.')

    def turn(self):
        print(f'Машина {self.name} повернула направо.')
        print(f'Машина {self.name} повернула налево.')

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')
        if self.speed > 60:
            print(f'Сбавь газ, на {self.name} нельзя так гонять!')
        else:
            print(f'Это разрешенная скорость для {self.name}')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость {self.name} - {self.speed}')
        if self.speed > 40:
            print(f'Сбавь газ, на {self.name} нельзя так гонять!')
        else:
            print(f'Это разрешенная скорость для {self.name}')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

skoda = TownCar(70, 'White', 'Skoda Octavia', False)
ferrari = SportCar(110, 'Red', 'Ferrari Roma', False)
ford = WorkCar(40, 'Blue', 'Ford Fiesta', False)
lada = PoliceCar(140, 'White and Blue', 'Lada Vesta Sport', True)

skoda.go()
skoda.turn()
skoda.show_speed()
skoda.stop()

ferrari.go()
ferrari.turn()
ferrari.show_speed()
ferrari.stop()

ford.go()
ford.turn()
ford.show_speed()
ford.stop()

lada.go()
lada.turn()
lada.show_speed()
lada.stop()
