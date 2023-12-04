'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-04 20:22:18
 # @ license: Mozilla Public License 2.0
 # @ description: the file contains the functions including regular expression used in the program
 '''

import re

from config.Name import kData_File_Format

def getHAndMaFromDatabaseFile(database_file: str) -> tuple:
    # get the first line of the file, which should look like 'H9.5Ma0.94'
    with open(database_file, 'r') as f:
        first_line: str = f.readline()
        pass
    # get the H and Ma
    H: float = float(re.findall(r'H\d+\.\d+', first_line)[0][1:])
    Ma: float = float(re.findall(r'Ma\d+\.\d+', first_line)[0][2:])
    return H, Ma
    pass

def getHAndMaFromSensorsFile(sensors_file: str) -> tuple:
    return getHAndMaFromDatabaseFile(sensors_file)
    pass

def getDomainFilesList(files_list: list) -> list:
    # get the domain files list from files_list
    # while the domain file should look like
    # "domain01.dat", in which case sensitive should be ignored
    domain_files_list: list = []
    pattern: str = re.compile(r"[Dd][Oo][Mm][Aa][Ii][Nn]\d+" + kData_File_Format)
    for file in files_list:
        whether_match = re.match(pattern, file)
        if whether_match == None:
            continue
            pass
        else:
            domain_files_list.append(whether_match.group())
            pass
        pass
    domain_files_list.sort()
    return domain_files_list
    pass

print("utils: RegularExpression.py is imported.")