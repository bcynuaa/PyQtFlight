'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-04 19:50:13
 # @ license: Mozilla Public License 2.0
 # @ description: the file contains the name used in the program
 '''

import time

# -------------------------------------------------------------------------------------------------

kSplit_Line: str = "--------------------------------------------------"

kData_File_Format: str = ".dat"
kDefault_Simulation_Name: str = "simulation"
kDefault_Flight_Test_Name: str = "flight_test"

# -------------------------------------------------------------------------------------------------

kScalarsList: list = ["ax", "ay", "az"]
kDefault_Scalar: str = "az"

# -------------------------------------------------------------------------------------------------

kTime_Domain_XLabel: str = "Time (s)"
kTime_Domain_YLabel: str = "Amplitude"
kFrequency_Domain_XLabel: str = "Frequency (Hz)"
kFrequency_Domain_YLabel: str = "Amplitude"

def getYlabel(i: int) -> str:
    """get the ylabel of time domain

    Args:
        i (int): the index of the ylabel

    Returns:
        str: the ylabel of time domain
    """
    if i == -1:
        return "i"
        pass
    else:
        return str(i+1)
        pass
    pass

# -------------------------------------------------------------------------------------------------

kTime_Format: str = r"%H:%M:%S-%Y-%m-%d"

def getCurrentTime() -> str:
    return time.strftime(
        kTime_Format,
        time.gmtime(time.time())
    ) + "\n"
    pass

kWelcome_Title: str = "Hello, PyQtFlightTest!"
kWelcome_Info: str = "\
Welcome to use PyQtFlightTest!\n\n\
This software is used to display aircraft's motion with data from Prof. Guo and his research group.\n\n\
Here're the things you need to know.\n\
    1. The current window is used to show output information.\n\
    2. The window on right side is used to display signals with an open-source python package matplotlib.\n\
    3. The window on the top of right side is used to display 3D geometry with an open-source python package pyvista.\n\
    4. You may load data and export the progress as video or gif via clicking menubar 'File'.\n\
    5. You may see the 2D and 3D information in new window via clicking menubar 'View'.\n\
    6. You may change some settings via clicking menubar 'Option'.\n\
    7. You may use some tools built-in via clicking 'Tools'.\n\n\
Warning: \n\
    1. This software is developed all with open-source's packages and languages, so the safety issue is not a concern.\n\
    2. All copy right of this software belongs to Prof. Guo and his research group.\n\
"

kList_Widget_Dict: dict = {
    0: "主窗口",
    1: "信号处理界面",
    2: "仿真分析界面"
}

kTab_Name_Time_Domain: str = "时域信号"
kTab_Name_Frequency_Domain: str = "频域信号"

# -------------------------------------------------------------------------------------------------

print("config: Name.py is imported.")