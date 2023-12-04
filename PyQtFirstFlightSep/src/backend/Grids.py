'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-21 22:10:39
 # @ description: backend for Grids
 '''


import os
import numpy as np

from src.config.libs.PyvistaConfig import pyvista
from src.config.backend.GridsConfig import *

from src.backend.DomainsWithModes import DomainsWithModes
from src.backend.Sensors import Sensors

class Grids:
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        self.domains_loaded: bool = False
        self.standard_mode_response_loaded: bool = False
        self.map_matrix_loaded: bool = False
        self.basic_magnification: float = basic_magnification
        self.compared_sensor_index: int = compared_sensor_index
        self.domains_with_modes: DomainsWithModes = DomainsWithModes()
        self.sensors: Sensors = Sensors()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def setBasicMagnification(self, basic_magnification: float) -> None:
        self.basic_magnification = basic_magnification
        pass
    
    def setComparedSensorIndex(self, compared_sensor_index: int) -> None:
        self.compared_sensor_index = compared_sensor_index
        self.allLoaded()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def loadDomainsFromPath(self, data_path: str) -> None:
        self.domains_with_modes.loadDomainFilesFromPath(data_path)
        self.domains_loaded = True
        self.__makeGrids()
        pass
    
    def __makeGrids(self) -> None:
        self.flight_test_grid: pyvista.UnstructuredGrid = \
            self.domains_with_modes.unstructured_grid.copy()
        self.simulation_grid: pyvista.UnstructuredGrid = \
            self.domains_with_modes.unstructured_grid.copy()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def loadMapMatrix(self, map_matrix_filename: str) -> None:
        self.sensors.loadMapMatrix(map_matrix_filename)
        self.map_matrix_loaded = True
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def loadStandardModeResponse(self, standard_mode_response_filename: str) -> None:
        standard_mode_response_filename_base: str = \
            os.path.basename(standard_mode_response_filename)
        if standard_mode_response_file_regular_expression_pattern.match( \
            standard_mode_response_filename_base) == None:
            print("error: Grids.loadStandardModeResponse: invalid file name")
            pass
        else:
            self.standard_mode_response: np.ndarray = np.loadtxt( \
                standard_mode_response_filename, skiprows=standard_mode_response_file_skiprows, \
                    max_rows=standard_mode_response_file_max_rows)
            self.standard_mode_response_loaded = True
            self.n_standard_modes: int = self.standard_mode_response.shape[0]
            self.standard_mode_response_filename: str = standard_mode_response_filename
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def checkModes(self) -> bool:
        if self.domains_with_modes.n_modes == self.sensors.n_modes == \
            self.n_standard_modes:
            return True
            pass
        else:
            return False
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeStandardMode(self) -> None:
        self.standard_sensor_response: np.ndarray = \
            self.sensors.modeToSensor(self.standard_mode_response)
        self.standard_compared_sensor_response: float = \
            self.standard_sensor_response[self.compared_sensor_index]
        self.standard_mode_shape: np.ndarray = \
            self.domains_with_modes.getModeShape(self.standard_mode_response)
        pass
    
    def allLoaded(self) -> bool:
        if self.domains_loaded == True and \
            self.map_matrix_loaded == True and \
                self.standard_mode_response_loaded == True:
            if self.checkModes() == True:
                self.__makeStandardMode()
                return True
                pass
            else:
                print("error: Grids.allLoaded: modes not matched")
                return False
                pass
            pass
        else:
            print("error: Grids.allLoaded: not all loaded")
            return False
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    # ! although getFactor and getFactors are similar or even can be merged into one function,
    # ! for safety and debugging, i still keep them as two functions
    # ! watch out for the difference between them
    
    def __getFactor(self, flight_test_sensor_response: np.ndarray) -> float:
        factor: float =  flight_test_sensor_response[self.compared_sensor_index] / \
            self.standard_compared_sensor_response
        return factor
        pass
    
    def __getFactors(self, flight_test_sensor_responses: np.ndarray) -> np.ndarray:
        # here assuming flight_test_sensor_responses is a 2D array
        # flight_test_sensor_responses.shape = (n_samples, n_sensors)
        factors: np.ndarray = flight_test_sensor_responses[:, self.compared_sensor_index] / \
            self.standard_compared_sensor_response
        return factors
        pass
    
    def getSimulationSensorResponse(self, flight_test_sensor_response: np.ndarray) -> np.ndarray:
        factor: float = self.__getFactor(flight_test_sensor_response)
        simulation_sensor_response: np.ndarray = factor * self.standard_sensor_response
        return simulation_sensor_response
        pass
    
    def getSimulationSensorResponses(self, flight_test_sensor_responses: np.ndarray) -> np.ndarray:
        factors: np.ndarray = self.__getFactors(flight_test_sensor_responses)
        simulation_sensor_responses: np.ndarray = \
            np.multiply(factors.reshape(-1, 1), self.standard_sensor_response)
        return simulation_sensor_responses
        pass
    
    def updateGrids(self, flight_test_sensor_response: np.ndarray) -> None:
        flight_test_mode_response: np.ndarray = \
            self.sensors.sensorToMode(flight_test_sensor_response)
        self.domains_with_modes.addModeResponseToGrid(self.flight_test_grid, \
            flight_test_mode_response, self.basic_magnification)
        factor: float = self.__getFactor(flight_test_sensor_response)
        simulation_mode_shape: np.ndarray = \
            self.standard_mode_shape * factor
        self.domains_with_modes.addModeShapeToGrid(self.simulation_grid, \
            simulation_mode_shape, self.basic_magnification)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("backend: Grids.py is imported")