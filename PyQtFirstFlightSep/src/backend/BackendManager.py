'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-28 23:46:53
 # @ description: bacend for BackendManager
 '''

import time
import numpy as np
import pandas as pd

from src.config.libs.PyvistaConfig import *
from src.config.backend.BackendManagerConfig import *

from src.decorator.Clock import clock

from src.backend.Grids import Grids
from src.backend.DataStream import DataStream

class BackendManager:
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        self.backend_built: bool = False
        self.bars_index_list: list = []
        self.grids: Grids = Grids()
        self.data_stream: DataStream = DataStream()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def isBuilt(self) -> bool:
        return self.backend_built
        pass
    
    def isEmpty(self) -> bool:
        return self.data_stream.isEmpty()
        pass
    
    def isUpdated(self) -> bool:
        return self.data_stream.isUpdated()
        pass
    
    def getSensorNumber(self) -> int:
        return self.grids.sensors.n_sensors
        pass
    
    def getModeNumber(self) -> int:
        return self.grids.domains_with_modes.n_modes
        pass
    
    def getCurvesNumber(self) -> int:
        return len(curves_sensor_index_list)
        pass
    
    def getBarsNumber(self) -> int:
        return len(self.bars_index_list)
        pass
    
    def getFlightTestGrid(self) -> pyvista.UnstructuredGrid:
        return self.grids.flight_test_grid
        pass
    
    def getSimulationGrid(self) -> pyvista.UnstructuredGrid:
        return self.grids.simulation_grid
        pass
    
    def getDataStreamMainDataFrameRowsNumber(self) -> int:
        return self.data_stream.main_dataframe.shape[0]
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def setBasicMagnification(self, basic_magnification: float) -> None:
        self.grids.setBasicMagnification(basic_magnification)
        pass
    
    def setComparedSensorIndex(self, compared_sensor_index: int) -> None:
        self.grids.setComparedSensorIndex(compared_sensor_index)
        pass
    
    def setFirstColumnIndex(self, first_column_index: int) -> None:
        self.data_stream.setFirstColumnIndex(first_column_index)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def loadDomainsFromPath(self, data_path: str) -> None:
        self.grids.loadDomainsFromPath(data_path)
        self.buildBackend()
        pass
    
    def loadMapMatrix(self, map_matrix_filename: str) -> None:
        self.grids.loadMapMatrix(map_matrix_filename)
        if bars_sensor_number_reorder_activated == True:
            self.bars_index_list = bars_sensor_number_reorder_index_list
            pass
        else:
            self.bars_index_list: list = []
            for index in range(self.getSensorNumber()):
                if index not in bars_sensor_number_except_index_list:
                    self.bars_index_list.append(index)
                    pass
                pass
            pass
        self.buildBackend()
        pass
    
    def loadStandardModeResponse(self, standard_mode_response_filename: str) -> None:
        self.grids.loadStandardModeResponse(standard_mode_response_filename)
        self.buildBackend()
        pass
    
    def buildBackend(self) -> None:
        if self.grids.allLoaded() == True:
            self.data_stream.setSensorNumber(self.getSensorNumber())
            self.backend_built = True
            print("BackendManager.buildBackend() succeeded")
            print("number of sensors: %d" % self.getSensorNumber())
            print("number of modes: %d" % self.getModeNumber())
            pass
        else:
            print("waning: BackendManager.buildBackend() failed, grids may have things not loaded")
            print("info: domains loaded: %s" % str(self.grids.domains_loaded))
            print("info: map matrix loaded: %s" % str(self.grids.map_matrix_loaded))
            print("info: standard mode response loaded: %s" % \
                str(self.grids.standard_mode_response_loaded))
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def readLatestData(self, latest_data_filename: str) -> None:
        self.data_stream.readLatestData(latest_data_filename)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def getLatestTimeDataForCurves(self) -> np.ndarray:
        return self.data_stream.getLatestTimeDataForCurves()
        pass
    
    def getLatestFlightTestSensorDataForCurves(self) -> np.ndarray:
        return self.data_stream.getLatestSensorDataForCurves()[:, curves_sensor_index_list]
        pass
    
    def getLatestSimulationSensorDataForCurves(self) -> np.ndarray:
        return self.grids.getSimulationSensorResponses( \
            self.data_stream.getLatestSensorDataForCurves())[:, curves_sensor_index_list]
        pass
    
    def getLatestSensorDataForGrids(self) -> np.ndarray:
        return self.data_stream.getLatestSensorDataForGrids()
        pass
    
    def getLatestSensorDataForBars(self) -> np.ndarray:
        flight_test_sensor_data_for_bars: np.ndarray = \
            self.data_stream.getLatestSensorDataForBars()
        simulation_sensor_data_for_bars: np.ndarray = self.grids.getSimulationSensorResponses( \
            flight_test_sensor_data_for_bars)
        flight_test_sensors_amplitude: np.ndarray = ( \
            np.max(flight_test_sensor_data_for_bars, axis = 0) - \
                np.min(flight_test_sensor_data_for_bars, axis = 0) ) / bars_devide
        simulation_sensors_amplitude: np.ndarray = ( \
            np.max(simulation_sensor_data_for_bars, axis = 0) - \
                np.min(simulation_sensor_data_for_bars, axis = 0) ) / bars_devide
        bars_amplitude: np.ndarray = np.abs( \
            flight_test_sensors_amplitude - simulation_sensors_amplitude)[self.bars_index_list]
        # * bars_value_limit, add on date 2023-08-13
        bars_amplitude[bars_amplitude > bars_value_limit] = bars_value_limit
        return bars_amplitude
        pass
    
    def getLatestParametersMarkdownTable(self) -> str:
        return self.data_stream.getLatestParametersMarkdownTable()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    @clock
    def updateGrids(self) -> None:
        latest_sensor_data_for_grids: np.ndarray = \
            self.getLatestSensorDataForGrids()
        for i_sensor_data in range(latest_sensor_data_for_grids.shape[0]):
            self.grids.updateGrids(latest_sensor_data_for_grids[i_sensor_data, :])
            time.sleep(grids_sleep_time)
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    # * update on date 2023-08-13 for replay
    def getMainDataFrameCopy(self) -> pd.DataFrame:
        return self.data_stream.getMainDataFrameCopy()
        pass
    
    def setMainDataFrame(self, main_dataframe: pd.DataFrame) -> None:
        self.data_stream.setMainDataFrame(main_dataframe)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def saveDataStream(self, save_filename: str="") -> None:
        self.data_stream.saveDataStream(save_filename)
        pass
    
    def clearDataStream(self) -> None:
        self.data_stream.clearDataStream()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("backend: BackendManager.py is imported")