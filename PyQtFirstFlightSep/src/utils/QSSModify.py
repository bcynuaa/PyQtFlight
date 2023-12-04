'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-02 18:36:00
 # @ description: util for QSSModify
 '''

import re

def setFontSizeToQss(qss: str, font_size: int) -> str:
    qss_modified: str = re.sub(r"font-size: (\d+)pt;", r"font-size: " + str(font_size) + r"pt;", qss)
    return qss_modified
    pass

print("utils: QSSModify.py is imported.")