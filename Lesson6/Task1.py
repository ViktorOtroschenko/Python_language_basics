# Task1.
"""Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт."""

import time

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        start = 0
        while start < 3:
            print(f'Загорелся: {TrafficLight.__color[start]}')
            if start == 0:
                time.sleep(7)
            elif start == 1:
                time.sleep(2)
            elif start == 2:
                time.sleep(10)
            start += 1

TrafficLight = TrafficLight()
TrafficLight.running()