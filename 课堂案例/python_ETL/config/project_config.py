"""
    Author: AubreyChen
    Time: 2023/3/21 17:11
    File: project_config.py.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""
import time

# ################## --程序运行日志的配置项-- ###################
# 配置日志输出的根目录
log_root_path = "E:/学习文件/作业/操作系统/课堂案例/python_ETL/logs/"
# 配置日志输出的文件名
log_name = f'pyetl-{time.strftime("%Y%m%d-%H", time.localtime(time.time()))}.log'
"""
常见的时间格式化的格式：
%Y:4位数字的年份：2022
%m:2位数字的月份：05
%d:2位数字的日期：15
%H：24小时制的小时
%M：2位数字的分钟
%S：2位数字的秒
如果要格式化为：2022-05-15 10:05:55
%Y-%m-%d %H:%M:%S
"""
# ################## --程序运行日志的配置项-- ###################

# ################## --JSON订单数据采集的相关配置项 start-- ###################
# 被采集的JSON数据，在哪个文件夹
json_data_root_path = "E:/学习文件/作业/操作系统/课堂案例/python_ETL/pyetl-data-logs/json"


# ################## --JSON订单数据采集的相关配置项 end-- ###################

# ################## --MySQL相关配置项 start-- ###################
mysql_charset = "utf8"
# 元数据管理库的配置
metadata_host = "localhost"
metadata_user = "root"
metadata_password = "121019"
metadata_port = 3306


# 数据源数据库的配置


# 目标数据库的配置


# ################## --MySQL相关配置项 end-- ###################