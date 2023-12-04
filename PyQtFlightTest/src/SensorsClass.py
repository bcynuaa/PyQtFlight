'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-07 17:38:53
 # @ license: Mozilla Public License 2.0
 # @ description: the class of sensors
 '''

import numpy as np

from config.Name import kSplit_Line

class Sensors:
    
    """the class of sensors
    - `sensors_mode_dis_file: str` -> the file of the sensors mode displacement
    - `mode_dis_matrix: np.ndarray` -> the matrix of the mode displacement
    - `n_sensors: int` -> the number of the sensors
    - `n_gen_dis: int` -> the number of the modes
    """
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        self.method_flag: int = 0
        pass
    
    def __str__(self) -> str:
        info: str = kSplit_Line + "\n<Sensors>\n"
        info += "sensors mode displacement files: " + self.sensors_mode_dis_file + "\n"
        info += "number of sensors: " + str(self.n_sensors) + "\n"
        info += "number of general displacement: " + str(self.n_gen_dis) + "\n"
        info += kSplit_Line + "\n"
        return info
        pass
    
    def __repr__(self) -> str:
        return self.__str__()
        pass
    
    def getInfo(self) -> str:
        return self.__str__()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def loadSensorsModeDisFile(self, sensors_mode_dis_file: str) -> None:
        self.sensors_mode_dis_file: str = sensors_mode_dis_file
        self.mode_dis_matrix: np.ndarray = np.loadtxt(sensors_mode_dis_file, dtype=np.float64)
        self.n_sensors, self.n_gen_dis = self.mode_dis_matrix.shape
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def getGenDisResponse(self, sensors_response: np.ndarray) -> np.ndarray:
        return np.linalg.lstsq(self.mode_dis_matrix, sensors_response, rcond=None)[0]
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("src: SensorsToModeClass.py is imported.")