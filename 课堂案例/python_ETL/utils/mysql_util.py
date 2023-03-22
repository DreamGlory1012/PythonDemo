"""
    Author: AubreyChen
    Time: 2023/3/22 9:12
    File: mysql_util.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""
import pymysql
from config import project_config as conf
from utils import logging_util


class MySQLUtil:
    def __init__(self,
                 host=conf.metadata_host,
                 port=conf.metadata_port,
                 password=conf.metadata_password,
                 user=conf.metadata_user,
                 charset=conf.mysql_charset,
                 autocommit=False
                 ):
        self.conn = pymysql.Connection(
            host=host,
            port=port,
            password=password,
            user=user,
            charset=charset,
            autocommit=autocommit
        )

        self.logger = logging_util.init_logger()
        self.logger.debug(f"构建完成{conf.metadata_host}:{conf.metadata_port}的连接")

    def close_conn(self):
        if self.conn:
            self.conn.close()

    def select_db(self, db):
        # 选择使用的数据库
        self.conn.select_db(db)
        self.logger.debug('选择数据库：' + db)

    def query(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.logger.debug('执行了SQL查询语句：' + sql)
        return self.cursor.fetchall()

    def execute(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        self.logger.debug('执行了SQL语句：' + sql)
        if not self.conn.get_autocommit():
            self.conn.commit()
        cursor.close()

    def execute_without_autocommit(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        cursor.close()

    def check_table_exists(self, db_name, table_name):
        self.conn.select_db(db_name)
        tables = self.query('SHOW TABLES')
        return (table_name,) in tables

    def check_table_exists_and_create(self, db_name, table_name, create_cols):
        if not self.check_table_exists(db_name, table_name):
            self.conn.select_db(db_name)
            create_sql = f"create table {table_name} ({create_cols})"
            self.execute(create_sql)
            self.logger.debug('创建表SQL：' + create_sql)
