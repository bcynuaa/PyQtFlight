'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-07-23 00:07:33
 # @ description: backend for DataStream
 '''

import os
import time
import numpy as np
import pandas as pd

from src.config.backend.DataStreamConfig import *

from src.utils.Paths import assurePathExists

class DataStream:
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        self.sensor_columns_first_column_index: int = sensor_columns_first_column_index
        self.__makeSettings()
        self.setSensorNumber(1)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeSettings(self) -> None:
        self.is_updated: bool = False
        self.main_dataframe: pd.DataFrame = pd.DataFrame()
        self.latest_parameters_dataframe: pd.DataFrame = pd.DataFrame( \
            data=np.zeros([1, len(parameter_columns_index_list)]), \
                columns=parameter_columns_name_list)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeColumnsMappingDict(self) -> None:
        columns_mapping_dict_keys: list[int] = time_columns_component_index_list + \
            self.sensors_index_list + parameter_columns_index_list
        columns_mapping_dict_values: list[str] = time_columns_component_name_list + \
            self.sensors_name_list + parameter_columns_name_list
        self.columns_mapping_dict: dict = dict(zip(columns_mapping_dict_keys, \
            columns_mapping_dict_values))
        pass
    
    def setFirstColumnIndex(self, first_column_index: int) -> None:
        self.sensor_columns_first_column_index = first_column_index
        self.setSensorNumber(self.n_sensors)
        pass
    
    def setSensorNumber(self, n_sensors: int) -> None:
        self.n_sensors = n_sensors
        self.sensors_index_list: list[int] = list(np.arange(self.n_sensors, dtype=int) \
            + self.sensor_columns_first_column_index)
        self.sensors_name_list: list[str] = [sensor_columns_name + "%d" % (i+1) \
            for i in range(self.n_sensors)]
        self.__makeColumnsMappingDict()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def isEmpty(self) -> bool:
        return self.main_dataframe.empty
        pass
    
    def isUpdated(self) -> bool:
        return self.is_updated
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __checkTimeContinuity(self, temp_dataframe: pd.DataFrame) -> bool:
        if self.isEmpty() == True:
            return True
            pass
        else:
            return temp_dataframe[time_columns_name].values[0] > \
                self.main_dataframe[time_columns_name].values[-1]
            pass
        pass
    
    def readLatestData(self, latest_data_filename: str) -> None:
        latest_data_filename_base: str = os.path.basename(latest_data_filename)
        if latest_data_regular_expression_pattern.match(latest_data_filename_base) == None:
            print("error: DataStream.readLatestData(): invalid filename")
            pass
        else:
            temp_dataframe: pd.DataFrame = pd.read_csv(latest_data_filename, \
                skiprows=latest_data_skiprows, \
                    delim_whitespace=latest_data_delim_whitespace, \
                        header=latest_data_header, index_col=latest_data_index_col)
            temp_dataframe[time_columns_name] = time_columns_component_conversion_list @ \
                temp_dataframe.iloc[:, time_columns_component_index_list].values.T
            self.is_updated = self.__checkTimeContinuity(temp_dataframe)
            if self.is_updated == True:
                temp_dataframe.rename(columns=self.columns_mapping_dict, inplace=True)
                self.latest_parameters_dataframe = \
                    temp_dataframe.tail(1).iloc[:, parameter_columns_index_list]
                self.main_dataframe = pd.concat([self.main_dataframe, temp_dataframe], \
                    ignore_index=True)
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def getLatestTimeDataForCurves(self) -> np.ndarray:
        return self.main_dataframe.tail( \
            latest_sensor_data_curves_nrows)[time_columns_name].values
        pass
    
    def getLatestSensorDataForCurves(self) -> np.ndarray:
        return self.main_dataframe.tail( \
            latest_sensor_data_curves_nrows).iloc[:, self.sensors_index_list].values
        pass
    
    def getLatestSensorDataForBars(self) -> np.ndarray:
        return self.main_dataframe.tail( \
            latest_sensor_data_bars_nrows).iloc[:, self.sensors_index_list].values
        pass
    
    def getLatestSensorDataForGrids(self) -> np.ndarray:
        return self.main_dataframe.tail( \
            latest_sensor_data_grids_nrows).iloc[:, self.sensors_index_list].values
        pass
    
    def getLatestParametersMarkdownTable(self) -> str:
        latest_parameter_dataframe: pd.DataFrame = pd.DataFrame( \
            [ self.latest_parameters_dataframe.columns.to_list(), \
                list(self.latest_parameters_dataframe.values[0]) ])
        latest_markdown_dataframe: pd.DataFrame = pd.DataFrame( \
            latest_parameter_dataframe.values.T.reshape( \
                latest_parameter_dataframe.shape[1] // markdown_table_column_number, \
                    len(markdown_table_name_list)),
                        columns=markdown_table_name_list)
        return latest_markdown_dataframe.to_markdown( \
            index=markdown_table_index, colalign=markdown_table_align_list)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    # * update on date 2023-08-13 for replay
    def getMainDataFrameCopy(self) -> pd.DataFrame:
        return self.main_dataframe.copy()
        pass
    
    def setMainDataFrame(self, main_dataframe: pd.DataFrame) -> None:
        self.main_dataframe = main_dataframe
        self.latest_parameters_dataframe = \
            main_dataframe.tail(1).iloc[:, parameter_columns_index_list]
        self.is_updated = True
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __saveDataStreamWithoutCheck(self, save_filename: str) -> None:
        self.main_dataframe.to_csv(save_filename, sep=save_sep, \
            header=save_header, index=save_index)
        pass
    
    def saveDataStream(self, save_filename: str="") -> None:
        if save_filename == "":
            if save_activated == True:
                assurePathExists(save_path)
                save_filename = os.path.join(save_path, save_name + save_separator + \
                    time.strftime(save_time_format, time.localtime()) + save_format)
                self.__saveDataStreamWithoutCheck(save_filename)
                pass
            else:
                pass
            pass
        else:
            self.__saveDataStreamWithoutCheck(save_filename)
            pass
        pass
    
    def clearDataStream(self) -> None:
        self.__makeSettings()
        pass
    
    #----------------------------------------------------------------------------------------------
    
    pass

print("backend: DataStream.py is imported")