"""
    Author: AubreyChen
    Time: 2023/3/21 17:39
    File: file_util.py
    IDE: PyCharm 2021
    Motto: Always Be Coding.
"""
import os


def get_dir_files_list(path='./', recursive=True):
    dir_names = os.listdir(path)
    files = []
    for dir_name in dir_names:
        if os.path.isdir(dir_name):
            if recursive:
                files += get_dir_files_list(os.path.join(path, dir_name), True)
        else:
            files.append(dir_name)
    return files
