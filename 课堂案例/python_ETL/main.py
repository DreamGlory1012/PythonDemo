"""
    Author: AubreyChen
    Time: 2023/3/20 16:51
    File: main.py.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""
import logging
import unittest

logger = logging.getLogger("test")
logger.setLevel(10)
fmt = logging.Formatter('%(asctime)s-[%(levelname)s] - %(filename)s[%(lineno)d]:%(message)s')
file_handle = logging.FileHandler(
    filename='test.log', mode='a', encoding='utf8'
)
file_handle.setFormatter(fmt)
logger.addHandler(file_handle)
stream_handle = logging.StreamHandler()
stream_handle.setFormatter(fmt)
logger.addHandler(stream_handle)
logger.info('info message')
logger.debug('debug message')
logger.error('error message')
logger.fatal('fatal message')
logger.warning('warning message')
