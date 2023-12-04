# coding = "utf-8"
# author: bcynuaa
# date: 2023/05/04

###################################################################################################
# This file is used to generate things in MainWindow

import time
import re

WELLCOME_INFO: str = "\
    Welcome to use PyQtAeroelastic!\n\n\
    This software is used to display aircraft's motion with data from Prof. Guo and his research group.\n\n\
    Here're the things you need to know.\n\
        1. The current window is used to show output information.\n\
        2. The window below is used to display time domain signals with an open-source python package matplotlib.\n\
        3. The rightside window is used to display 3D geometry with an open-source python package pyvista.\n\
        4. You may load data and export the progress as video or gif via clicking menubar 'File'.\n\
        5. You may see the 2D and 3D information in new window via clicking menubar 'View'.\n\
        6. You may change some settings via clicking menubar 'Option'.\n\n\
    Warning: \n\
        1. This software is developed all with open-source's packages and languages, so the safety issue is not a concern.\n\
        2. All copy right of this software belongs to Prof. Guo and his research group.\n\
"

SPLIT_LINE: str = "\n----------------------------------------------------------------------\n"

TIME_FORMAT: str = r"%H:%M:%S-%Y-%m-%d"

###################################################################################################

def getCurrentTime() -> str:
    return time.strftime(
        TIME_FORMAT,
        time.gmtime(time.time())
    ) + "\n\n"
    pass

###################################################################################################

def stringToIndexList(string: str) -> list:
    index_list: list = list()
    num_pattern: re.Pattern = re.compile(r"\d+")
    num_range_pattern: re.Pattern = re.compile(r"\d+-\d+")
    num_list: list = num_pattern.findall(string)
    num_range_list: list = num_range_pattern.findall(string)
    for item in num_list:
        index_list.append(eval(item))
        pass
    for item in num_range_list:
        tmp_range_list: list = num_pattern.findall(item)
        start_num: int = int(eval(tmp_range_list[0]))
        end_num: int = int(eval(tmp_range_list[1]))
        for index in range(start_num, end_num+1):
            index_list.append(index)
            pass
        pass
    index_list = list(set(index_list))
    index_list.sort()
    return index_list
    pass

###################################################################################################

print("successfully generate basic things in MainWindow.\n")

###################################################################################################