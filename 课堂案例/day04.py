"""
    Author: AubreyChen
    Time: 2023/3/15 10:35
    File: day04.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""
import json
import os

from student import Student

student1 = Student("张峰", "男", 21, "12315", "大徒弟...")
student2 = Student("张铭逸", "男", 12, "18767675544", "超级乖..")
student3 = Student("陈婷", "女", 18, "19234345566", "女生..")

student_lists = [student1, student2, student3]
print(list(student_lists[0].__dict__.keys()))
file_path = os.path.dirname(__file__)
with open(os.path.join(file_path, 'stu1.json'), 'r', encoding='utf8') as fp:
    json.load(fp)

print(a)
