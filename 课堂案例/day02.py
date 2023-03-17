"""
    Author: AubreyChen
    Time: 2023/3/14 16:08
    File: day02.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""

class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f'{self.brand}启动发动机')

    def stop(self):
        print(f'{self.brand}正在刹车')
count = 300
class Teacher:
    count=100
    def __init__(self, name):
        self.name = name

    def driver(self, car:Car):
        car.start()
        print(f'{self.name}正在开车')

    def power_off(self, car):
        car.stop()
        print(f'{self.name}正在刹车')

    def cou(self):
        global count
        print(count)
    def cou2(self):
        print(self.count)
        print(self.count)
    @classmethod
    def cou3(cls):
        print(cls.count)




class Bike(Car):

    def start(self):
        print(f'{self.brand}开始起步')


class Metro(Car):

    def start(self):
        print(f'{self.brand}开始启动')

car = Metro("ofo")
teacher = Teacher("方坚")
teacher.driver(car)
teacher.power_off(car)
print(teacher.count)
teacher.cou()
teacher.cou2()
teacher.cou3()

print(f'{"开始":*^100}')

