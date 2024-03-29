# Task2
'''Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — ​ одежда​ , которая может иметь определенное название. К
типам одежды в этом проекте относятся ​ пальто ​ и ​ костюм​ . У этих типов одежды существуют
параметры: ​ размер ​ (для ​ пальто​) и ​ рост ​(для костюма). Это могут быть обычные числа: ​
V и  H​ , соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5)​ , для костюма ​ (2*H + 0.3)​ . Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора ​ @property.'''

from abc import ABC, abstractmethod

class Clothes(ABC):
    name = None

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def consumption(self):
        pass

class Coat(Clothes):
    name = 'Пальто'

    def __init__(self, v):
        self.v = v

    def __str__(self):
        return f'Размер {self.name}: {str(self.v)}'

    @property
    def consumption(self):
        return '{:.2f}'.format(self.v / 6.5 + 0.5)

class Costume(Clothes):
    name = 'Костюм'

    def __init__(self, h):
        self.h = h

    def __str__(self):
        return f'{self.name} размером: {str(self.h)}'

    @property
    def consumption(self):
        return '{:.2f}'.format(self.h * 2 + 0.3)

coat = Coat(50)
print(coat, f'\nТкани необходимо на {coat.name}:', coat.consumption)
costume = Costume(184)
print(costume, f'\nТкани необходимо на {costume.name}:', costume.consumption)
print(f'Общий расход ткани: {(float(coat.consumption) + float(costume.consumption))}')
