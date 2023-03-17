"""
    Author: AubreyChen
    Time: 2023/3/13 19:50
    File: day01.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""


class Father(object):

    def __init__(self,name,gender):
        self.name = "男"  # 方法
        self.gender = '王'

    # def get_Name(self):
    #     return self.__Name

    # def set_name(self, name):
    #     self.__name = name

    def run(self):
        print("跑得比兔子还快...")

    def a(self):
        print("12")

# 2.定义一个子类、继承自父类
class Son(Father):
    pass


# son = Son()
# # 4.结论( 子类拥有文类的属性和方法、简化了代码
# print(f"Son的属性:{son.sex}")
# son.run()

class Person(object):
    def __init__(self,name,gender):
        self.name =name
        self.gender =gender
        print("Person类__init__()。", "姓名：",self.name)
    def a(self):
        print("111")
class Student(Person,Father):
    def __init__(self,name,gender,score):
        pass
    def a(self):
        super(Person, self).a()
        super(Student, self).a()
        super().a()
        Father.a(self)
stu = Student("A",'V',12)
stu.a()
print(Student.__mro__)