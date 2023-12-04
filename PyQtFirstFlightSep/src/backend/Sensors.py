'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-21 22:10:39
 # @ description: backend for Sensors
 '''

import os
import numpy as np

from src.config.backend.SensorsConfig import *

class Sensors:
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        self.map_matrix_loaded: bool = False
        pass
    
    def __str__(self) -> str:
        info: str = "map matrix loaded: %s\n" % str(self.map_matrix_loaded)
        if self.map_matrix_loaded == False:
            pass
        else:
            info += "map matrix file name: %s\n" % self.map_matrix_filename
            info += "number of sensors: %d\n" % self.n_sensors
            info += "number of modes: %d" % self.n_modes
            pass
        return info
        pass
    
    def __repr__(self) -> str:
        return self.__str__()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def loadMapMatrix(self, map_matrix_filename: str) -> None:
        map_matrix_filename_base: str = os.path.basename(map_matrix_filename)
        if map_matrix_regular_expression_pattern.match(map_matrix_filename_base) == None:
            print("error: Sensors.loadMapMatrix: invalid file name")
            pass
        else:
            self.map_matrix: np.ndarray = np.loadtxt(map_matrix_filename, \
                skiprows=skiprows, dtype=np.float64)
            self.n_sensors, self.n_modes = self.map_matrix.shape
            self.map_matrix_filename: str = map_matrix_filename
            self.map_matrix_loaded = True
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def modeToSensor(self, mode_response: np.ndarray) -> np.ndarray:
        return self.map_matrix @ mode_response
        pass
    
    def sensorToMode(self, sensor_response: np.ndarray) -> np.ndarray:
        return np.linalg.lstsq(self.map_matrix, sensor_response, rcond=None)[0]
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("backend: Sensors.py is imported")