'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-06 17:18:21
 # @ description: utils for Paths
 '''

import os

def assurePathExists(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
        pass
    pass

print("utils: Paths.py is imported")