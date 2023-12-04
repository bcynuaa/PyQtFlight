'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-04 22:10:13
 # @ license: Mozilla Public License 2.0
 # @ description: the file contains functions for sub-dict used in the program
 '''
 
import numpy as np

def insertToSubDict(origin_dict: dict, main_key, sub_key, sub_value) -> None:
    # this dict should look like: origin_dict[main_key][sub_key] = sub_value
    if main_key not in origin_dict:
        origin_dict[main_key] = dict()
        origin_dict[main_key][sub_key] = sub_value
        pass
    else:
        origin_dict[main_key][sub_key] = sub_value
        pass
    pass

def getSubDictKeys(origin_dict: dict) -> list:
    # this dict should look like: origin_dict[main_key][sub_key] = sub_value
    # this function is to get the sub-dict's keys like: [(main_key1, sub_key1), ...]
    sub_dict_keys: list = []
    for main_key in origin_dict:
        for sub_key in origin_dict[main_key]:
            sub_dict_keys.append((main_key, sub_key))
            pass
        pass
    return sub_dict_keys
    pass

def getCloestSubDictKeys(origin_dict: dict,\
    main_key_in: np.float64, sub_key_in: np.float64) -> tuple:
    index_main: np.int64 = np.argmin(np.abs(np.array(list(origin_dict.keys())) - main_key_in))
    main_key: np.float64 = list(origin_dict.keys())[index_main]
    index_sub: np.int64 = np.argmin(np.abs(np.array(list(origin_dict[main_key].keys())) - sub_key_in))
    sub_key: np.float64 = list(origin_dict[main_key].keys())[index_sub]
    return (main_key, sub_key)
    pass

print("utils: SubDict.py is imported.")