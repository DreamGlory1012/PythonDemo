"""
    Author: AubreyChen
    Time: 2023/3/17 15:22
    File: day05.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""


def outer(func):
    def inner():
        print("inner...")
        func()

    return inner


def outer2(*args, **kwargs):
    def inner(func):
        def inner_in(*args, **kwargs):
            print(args)
            print(kwargs)
            result = func(*args, **kwargs)
            return result

        return inner_in

    return inner


@outer
def test():
    print("test...")


@outer2("arg1", 'arg2')
def test2(*args, **kwargs):
    print("test2...")
    # return x + y


print(test2(3, 5))
