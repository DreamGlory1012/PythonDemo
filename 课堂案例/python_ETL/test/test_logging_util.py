"""
    Author: AubreyChen
    Time: 2023/3/21 17:12
    File: test_logging_util.py.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""
from unittest import TestCase
import logging
from utils import logging_util

class LoggingUtilTest(TestCase):
    def setUp(self) -> None:
        pass

    def test_get_logger(self):
        logger = logging_util.init_logger()
        result = isinstance(logger, logging.RootLogger)
        self.assertEqual(True, result)