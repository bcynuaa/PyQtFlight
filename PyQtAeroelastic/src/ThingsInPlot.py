# coding = "utf-8"
# author: bcynuaa
# date: 2023/05/04

###################################################################################################
# This file is used to generate things in plot

def getYLable(index: int = None) -> str:
    ylabel_head: str = r"$q_"
    ylabel_tail: str = r"(t)$"
    if type(index) == str:
        ylabel: str = ylabel_head + i + ylabel_tail
        pass
    elif type(index) == float:
        i = int(round(index))
        ylabel: str = ylabel_head + str(i+1) + ylabel_tail
        pass
    elif type(index) == int:
        ylabel: str = ylabel_head + str(index+1) + ylabel_tail
        pass
    else:
        ylabel: str = ylabel_head + "i" + ylabel_tail
        pass
    return ylabel
    pass

DEFAULT_XLABEL: str = r"time $t$"
DEFAULT_YLABEL: str = getYLable()
DEFAULT_TITLE: str = r"Displacement Response Here"

print("successfully generate basic things in plot.\n")

###################################################################################################