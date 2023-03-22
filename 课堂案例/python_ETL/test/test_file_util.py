"""
    Author: AubreyChen
    Time: 2023/3/21 17:39
    File: test_file_util.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""
import os
from unittest import TestCase
from utils import file_util

class FileUtilTest(TestCase):
    def setUp(self) -> None:
        """等同于__init__"""
        # os.path.dirname(os.getcwd())获取当前工程的根目录
        self.project_root_path = os.path.dirname(os.getcwd())

    def test_get_dir_files_list(self):
        test_path = f"{self.project_root_path}/test/test_dir"
        # 先测试不递归
        result = file_util.get_dir_files_list(test_path, recursive=False)
        # result记录的是绝对路径，我们需要将文件的名字取出来
        names = []  # 定义一个list记录结果的文件名
        for i in result:
            # os.path.basename可以从路径中取出最后的文件名
            names.append(os.path.basename(i))
        # 为了避免结果的顺序产生测试失败，将names对象升序
        names.sort()  # 将 list 升序 [1 3 2], [1 2 3]
        self.assertEqual(["1", "2"], names)

        # 再测试递归
        result = file_util.get_dir_files_list(test_path, recursive=True)
        # result记录的是绝对路径，我们需要将文件的名字取出来
        names = []  # 定义一个list记录结果的文件名
        for i in result:
            # os.path.basename可以从路径中取出最后的文件名
            names.append(os.path.basename(i))
        names.sort()
        self.assertEqual(["1", "2", "3", "4", "5"], names)