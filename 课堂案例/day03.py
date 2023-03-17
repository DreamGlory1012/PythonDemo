"""
    Author: AubreyChen
    Time: 2023/3/15 9:58
    File: day03.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""
import multiprocessing
from multiprocessing.pool import Pool
import multiprocessing
import threading
import os
import time

lock = threading.Lock()


def main(current_path):
    for i in range(10000):
        time.sleep(0.5)
        print(os.getpid())
        print(os.getppid())
        print(current_path)


def main2(num):
    lock.acquire()
    print(num)
    lock.release()


if __name__ == '__main__':
    pro = multiprocessing.Process(target=main, name='子进程1', daemon=True, kwargs={'current_path': __file__})
    # pro.start()
    # pro.join()
    pros = Pool()
    thread = threading.Thread(target=main,name='子线程1',args=(1,),daemon=True)
    thread.start()
    thread.join()
    # pros.map(main2, [i for i in range(1, 100)])
