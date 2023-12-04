# coding: "utf-8"
# author: bcynuaa
# date: 2023/05/18

###################################################################################################
# This file is used to do *re* pattern match

import re

def getDomainFilesList(data_file_list: list) -> list:
    """find the domain files from the data file list
    """
    domain_files_list: list = list()
    pattern: str = re.compile(r"[Dd][Oo][Mm][Aa][Ii][Nn]\d+\.dat")
    for item in data_file_list:
        whether_match = re.match(pattern, item)
        if whether_match == None:
            continue
            pass
        else:
            domain_files_list.append(whether_match.group())
        pass
    domain_files_list.sort()
    return domain_files_list
    pass

print("Pattern match has been loaded.")

###################################################################################################