'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-08 03:09:38
 # @ description: interface for MainWindowLogic
 '''

from src.interface.MainWindowUI import MainWindowUI
from src.interface.FileDialogs import *
from src.interface.InputDialogs import *
from src.interface.MessageBoxes import *

class MainWindowLogic(MainWindowUI):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
        self.__makeMenuBarLogicConnections()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def loadJsonFile(self) -> None:
        json_filename, _ = loadJsonFileQFileDialog(self)
        if json_filename == "":
            pass
        else:
            try:
                super().loadJsonFile(json_filename)
                loadJsonFileSucceededQMessageBox(self, \
                    self.backend_manager.getModeNumber(), \
                        self.backend_manager.getSensorNumber())
                pass
            except:
                loadJsonFileFailedQMessageBox(self)
                pass
            pass
        pass
    
    def saveDataStream(self) -> None:
        data_stream_filename, _ = saveDataStreamQFileDialog(self)
        if data_stream_filename == "":
            pass
        else:
            super().saveDataStream(data_stream_filename)
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def replay(self) -> None:
        if self.backend_manager.isEmpty() == True:
            return
            pass
        main_dataframe_n_rows: int = self.backend_manager.getDataStreamMainDataFrameRowsNumber()
        main_dataframe_n_rows = main_dataframe_n_rows - 1
        start_row, ok_pressed = replayStartRowQInputDialog(self, \
            0, 0, main_dataframe_n_rows)
        if ok_pressed == True:
            end_row, ok_pressed = replayEndRowQInputDialog(self, \
                main_dataframe_n_rows, 0, main_dataframe_n_rows)
            if ok_pressed == True:
                interval_row, ok_pressed = replayIntervalRowQInputDialog(self, \
                    32, 1, main_dataframe_n_rows)
                if ok_pressed == True:
                    super().replay(start_row, end_row, interval_row)
                    pass
                else:
                    pass
                pass
            pass
        else:
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeMenuBarFilesLogicConnections(self) -> None:
        self.menu_bar_files_load_data_load_json_file.triggered.connect(self.loadJsonFile)
        self.menu_bar_files_data_stream_save_data_stream.triggered.connect(self.saveDataStream)
        self.menu_bar_files_data_stream_clear_data_stream.triggered.connect(self.clearDataStream)
        pass
    
    def __makeMenuBarEditLogicConnections(self) -> None:
        # TODO: add logic connections for menuBarEdit
        pass
    
    def __makeMenuBarOptionsLogicConnections(self) -> None:
        self.menu_bar_options_start_monitoring.triggered.connect(self.startMonitoring)
        self.menu_bar_options_end_monitoring.triggered.connect(self.endMonitoring)
        self.menu_bar_options_replay.triggered.connect(self.replay)
        pass
    
    def __makeMenuBarToolsLogicConnections(self) -> None:
        # TODO: add logic connections for menuBarTools
        pass
    
    def __makeMenuBarLogicConnections(self) -> None:
        self.__makeMenuBarFilesLogicConnections()
        self.__makeMenuBarEditLogicConnections()
        self.__makeMenuBarOptionsLogicConnections()
        self.__makeMenuBarToolsLogicConnections()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("interface: MainWindowLogic.py is imported")