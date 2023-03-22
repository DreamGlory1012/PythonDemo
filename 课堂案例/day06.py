"""
    Author: AubreyChen
    Time: 2023/3/19 20:57
    File: day06.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""
import datetime
import time
from datetime import timezone
# print(timezone(datetime.timedelta(0.5),'china')
from datetime import date
# print(datetime.timedelta(2.99,3)-datetime.timedelta(2,3))
# print(
# datetime.timedelta(2.99,3))
# print(datetime.time(20,21,30))
import datetime
print(type(datetime.datetime.today()))
print(datetime.datetime.now().strftime('%x %X'))
print(
datetime.datetime.strptime('2021821','%Y%m%d').date())
print(type(datetime.datetime.strptime('2021821','%Y%m%d').date()))