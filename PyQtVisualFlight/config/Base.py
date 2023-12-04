# coding: "utf-8"
# author: bcynuaa
# date: 2023/05/18

###################################################################################################
# This file is used to contain some basic static variables

DEFAULT_LHS_NAME: str = "flight_test"
DEFAULT_RHS_NAME: str = "simulation" 
DEFAULT_DATA_FORMAT: str = ".dat"

def observeFileName(flag: str) -> str:
    """ovserved file name

    Args:
        flag (str): "flight_test" or "simulation"

    Returns:
        str: path + flag + format
    """
    return flag + DEFAULT_DATA_FORMAT
    pass

print("Basic things have been loaded.")

###################################################################################################