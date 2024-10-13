from threading import Thread
from time import sleep
from datetime import datetime

class Knight(Thread):

    def __init__(self, name, power,):
        super().__init__()
        self.name = name
        self.power = power



    def run(self):
        print(f'{self.name}, на нас напали!')
        i = 0
        enemies = 100
        while enemies != 0:
            sleep(1)
            i += 1
            enemies = enemies - self.power
            print(f'{self.name} сражается {i} дней, осталось {enemies} воинов.')

        print(f'{self.name} одержал победу спустя {i} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()