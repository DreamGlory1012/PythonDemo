"""
    Author: AubreyChen
    Time: 2023/3/21 17:33
    File: logging_util.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""
"""
这个python文件的功能，是构建日志输出的模块
方便我们后续快速的在程序中方便的输入日志信息

Python中最常用的日志库，是一个叫做logging的模块
"""

import logging
from config import project_config as conf


# 先封装一个class，class提供基本的logger对象（没有啥属性，只有级别默认为INFO）
class Logging:
    def __init__(self, level=20):
        self.logger = logging.getLogger()
        self.logger.setLevel(level)


# 构建一个方法，我们可以通过这个方法返回所需的logger对象
def init_logger():
    # 初始化刚刚自己定义的Logging类，得到类中的logger对象
    logger = Logging().logger

    if logger.handlers:
        return logger

    # 对logger对象设置属性，比如输出到文件以及输出格式的设置
    file_handler = logging.FileHandler(
        filename=conf.log_root_path + conf.log_name,
        mode="a",
        encoding="UTF-8"
    )

    # 设置一个format输出格式
    fmt = logging.Formatter(
        "%(asctime)s - [%(levelname)s] - %(filename)s[%(lineno)d]: %(message)s"
    )

    # 将格式设置到文件的handler中
    file_handler.setFormatter(fmt)

    # 将文件输出的Handler设置给logger对象
    logger.addHandler(file_handler)

    return logger
