'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-02 21:42:59
 # @ description: interface for MainWindowUI
 '''

import os
import json
import pandas as pd
from PySide2.QtCore import Slot, Signal
from PySide2.QtWidgets import QMainWindow, QWidget
from PySide2.QtWidgets import QLabel
from PySide2.QtWidgets import QMenuBar, QMenu, QAction
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide2.QtGui import QCloseEvent, QResizeEvent
from PySide2.QtGui import QIcon

from src.config.LanguageConfig import encoding
from src.config.interface.MainWindowUIConfig import *

from src.decorator.Clock import clock
from src.decorator.NoError import noError

from src.utils.FileMonitorOnQThread import FileMonitorOnQThread
from src.utils.CallbackOnQThread import CallbackOnQThread

from src.backend.BackendManager import BackendManager
from src.widgets.WidgetsManager import WidgetsManager
from src.interface.MessageBoxes import *

class MainWindowUI(QMainWindow):
    
    parameters_browser_update_signal: Signal = Signal()
    sensor_bars_plotter_update_signal: Signal = Signal()
    flight_test_curves_plotter_update_signal: Signal = Signal()
    simulation_curves_plotter_update_signal: Signal = Signal()
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
        self.central_widget: QWidget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.__makeSettings()
        self.__makeMenuBar()
        self.__makeLayout()
        self.__makeBackendManager()
        self.__makeWidgetsManager()
        self.__makeFileMonitorOnQThread()
        self.__makeSignalConnections()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeSettings(self) -> None:
        self.setWindowTitle(window_title)
        self.setStyleSheet(main_window_ui_config_style)
        self.setWindowIcon(QIcon(window_icon))
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeMenuBarFiles(self) -> None:
        # menu bar: files
        self.menu_bar_files: QMenu = QMenu(self.menu_bar)
        self.menu_bar_files.setTitle(menu_bar_files_dict["text"])
        self.menu_bar.addAction(self.menu_bar_files.menuAction())
        # menu bar: files: load data
        self.menu_bar_files_load_data: QMenu = QMenu(self.menu_bar_files)
        self.menu_bar_files_load_data.setTitle(menu_bar_files_dict["values"]["load data"]["text"])
        self.menu_bar_files.addAction(self.menu_bar_files_load_data.menuAction())
        # menu bar: files: load data: load json file
        self.menu_bar_files_load_data_load_json_file: QAction = \
            QAction(self.menu_bar_files_load_data)
        self.menu_bar_files_load_data_load_json_file.setText( \
            menu_bar_files_dict["values"]["load data"]["values"]["load json file"]["text"])
        self.menu_bar_files_load_data.addAction( \
            self.menu_bar_files_load_data_load_json_file)
        # menu bar: files: data stream
        self.menu_bar_files_data_stream: QMenu = QMenu(self.menu_bar_files)
        self.menu_bar_files_data_stream.setTitle(menu_bar_files_dict["values"]["data stream"]["text"])
        self.menu_bar_files.addAction(self.menu_bar_files_data_stream.menuAction())
        # menu bar: files: data stream: save data stream
        self.menu_bar_files_data_stream_save_data_stream: QAction = \
            QAction(self.menu_bar_files_data_stream)
        self.menu_bar_files_data_stream_save_data_stream.setText( \
            menu_bar_files_dict["values"]["data stream"]["values"]["save data stream"]["text"])
        self.menu_bar_files_data_stream.addAction( \
            self.menu_bar_files_data_stream_save_data_stream)
        # menu bar: files: data stream: clear data stream
        self.menu_bar_files_data_stream_clear_data_stream: QAction = \
            QAction(self.menu_bar_files_data_stream)
        self.menu_bar_files_data_stream_clear_data_stream.setText( \
            menu_bar_files_dict["values"]["data stream"]["values"]["clear data stream"]["text"])
        self.menu_bar_files_data_stream.addAction( \
            self.menu_bar_files_data_stream_clear_data_stream)
        pass
    
    def __makeMenuBarEdit(self) -> None:
        # menu bar: edit
        self.menu_bar_edit: QMenu = QMenu(self.menu_bar)
        self.menu_bar_edit.setTitle(menu_bar_edit_dict["text"])
        self.menu_bar.addAction(self.menu_bar_edit.menuAction())
        pass
    
    def __makeMenuBarOptions(self) -> None:
        # menu bar: options
        self.menu_bar_options: QMenu = QMenu(self.menu_bar)
        self.menu_bar_options.setTitle(menu_bar_options_dict["text"])
        self.menu_bar.addAction(self.menu_bar_options.menuAction())
        # menu bar: options: start monitoring
        self.menu_bar_options_start_monitoring: QAction = \
            self.menu_bar_options.addAction( \
                menu_bar_options_dict["values"]["start monitoring"]["text"])
        self.menu_bar_options_start_monitoring.setText( \
            menu_bar_options_dict["values"]["start monitoring"]["text"])
        # menu bar: options: end monitoring
        self.menu_bar_options_end_monitoring: QAction = \
            self.menu_bar_options.addAction( \
                menu_bar_options_dict["values"]["end monitoring"]["text"])
        self.menu_bar_options_end_monitoring.setText( \
            menu_bar_options_dict["values"]["end monitoring"]["text"])
        # menu bar: options: replay
        self.menu_bar_options_replay: QAction = \
            self.menu_bar_options.addAction( \
                menu_bar_options_dict["values"]["replay"]["text"])
        self.menu_bar_options_replay.setText( \
            menu_bar_options_dict["values"]["replay"]["text"])
        pass
    
    def __makeMenuBarTools(self) -> None:
        # menu bar: tools
        self.menu_bar_tools: QMenu = QMenu(self.menu_bar)
        self.menu_bar_tools.setTitle(menu_bar_tools_dict["text"])
        self.menu_bar.addAction(self.menu_bar_tools.menuAction())
        # menu bar: tools: run executables
        self.menu_bar_tools_run_executables: QAction = \
            self.menu_bar_tools.addAction( \
                menu_bar_tools_dict["values"]["run executables"]["text"])
        self.menu_bar_tools_run_executables.setText( \
            menu_bar_tools_dict["values"]["run executables"]["text"])
        pass
    
    def __makeMenuBar(self) -> None:
        self.menu_bar: QMenuBar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)
        self.__makeMenuBarFiles()
        self.__makeMenuBarEdit()
        self.__makeMenuBarOptions()
        self.__makeMenuBarTools()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeGridPlotterLayout(self) -> None:
        # flight test grid plotter layout
        self.flight_test_grid_plotter_layout: QVBoxLayout = QVBoxLayout()
        self.grid_plotter_layout.addLayout(self.flight_test_grid_plotter_layout)
        self.flight_test_grid_plotter_label: QLabel = QLabel()
        self.flight_test_grid_plotter_label.setText( \
            labels_dict["flight test grid plotter"]["text"])
        self.flight_test_grid_plotter_layout.addWidget(self.flight_test_grid_plotter_label)
        # simulation grid plotter layout
        self.simulation_grid_plotter_layout: QVBoxLayout = QVBoxLayout()
        self.grid_plotter_layout.addLayout(self.simulation_grid_plotter_layout)
        self.simulation_grid_plotter_label: QLabel = QLabel()
        self.simulation_grid_plotter_label.setText( \
            labels_dict["simulation grid plotter"]["text"])
        self.simulation_grid_plotter_layout.addWidget(self.simulation_grid_plotter_label)
        pass
    
    def __makeCurvesPlotterLayout(self) -> None:
        self.flight_test_curves_plotter_layout: QVBoxLayout = QVBoxLayout()
        self.simulation_curves_plotter_layout: QVBoxLayout = QVBoxLayout()
        self.curves_plotter_layout.addLayout(self.flight_test_curves_plotter_layout)
        self.curves_plotter_layout.addLayout(self.simulation_curves_plotter_layout)
        pass
    
    def __makeLivePlotterLayout(self) -> None:
        self.sensor_bars_plotter_layout: QVBoxLayout = QVBoxLayout()
        self.curves_plotter_layout: QHBoxLayout = QHBoxLayout()
        self.live_plotter_layout.addLayout(self.sensor_bars_plotter_layout)
        self.live_plotter_layout.addLayout(self.curves_plotter_layout)
        self.__makeCurvesPlotterLayout()
        pass
    
    def __makeExceptGridPlotterLayout(self) -> None:
        self.parameters_browser_layout: QVBoxLayout = QVBoxLayout()
        self.live_plotter_layout: QVBoxLayout = QVBoxLayout()
        self.except_grid_plotter_layout.addLayout(self.parameters_browser_layout)
        self.except_grid_plotter_layout.addLayout(self.live_plotter_layout)
        self.__makeLivePlotterLayout()
        pass
    
    def __makeLayout(self) -> None:
        self.central_layout: QVBoxLayout = QVBoxLayout(self.central_widget)
        self.grid_plotter_layout: QHBoxLayout = QHBoxLayout()
        self.except_grid_plotter_layout: QHBoxLayout = QHBoxLayout()
        self.central_layout.addLayout(self.grid_plotter_layout)
        self.central_layout.addLayout(self.except_grid_plotter_layout)
        self.__makeGridPlotterLayout()
        self.__makeExceptGridPlotterLayout()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeBackendManager(self) -> None:
        self.backend_manager: BackendManager = BackendManager()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeWidgetsManager(self) -> None:
        self.widgets_manager: WidgetsManager = WidgetsManager()
        self.widgets_manager.setParent(self)
        # grid plotter
        self.flight_test_grid_plotter_layout.addWidget( \
            self.widgets_manager.getFlightTestGridPlotter())
        self.simulation_grid_plotter_layout.addWidget( \
            self.widgets_manager.getSimulationGridPlotter())
        # parameters browser
        self.parameters_browser_layout.addWidget( \
            self.widgets_manager.getParametersBrowser())
        self.__updateParametersBrowser()
        # bars plotter
        self.sensor_bars_plotter_layout.addWidget( \
            self.widgets_manager.getSensorBarsPlotter())
        # curves plotter
        self.flight_test_curves_plotter_layout.addWidget( \
            self.widgets_manager.getFlightTestCurvesPlotter())
        self.simulation_curves_plotter_layout.addWidget( \
            self.widgets_manager.getSimulationCurvesPlotter())
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeFileMonitorOnQThread(self) -> None:
        self.file_monitor_on_qthread: FileMonitorOnQThread = FileMonitorOnQThread()
        self.file_monitor_on_qthread.setParent(self)
        self.file_monitor_on_qthread.setModifiedCallback( \
            self.readLatestDataAndUpdateWidgets)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeSignalConnections(self) -> None:
        self.parameters_browser_update_signal.connect(self.__updateParametersBrowser)
        self.sensor_bars_plotter_update_signal.connect(self.__updateSensorBarsPlotter)
        self.flight_test_curves_plotter_update_signal.connect( \
            self.__updateFlightTestCurvesPlotter)
        self.simulation_curves_plotter_update_signal.connect( \
            self.__updateSimulationCurvesPlotter)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeGridConnections(self) -> None:
        self.widgets_manager.connectWithFlightTestGrid( \
            self.backend_manager.getFlightTestGrid())
        self.widgets_manager.connectWithSimulationGrid( \
            self.backend_manager.getSimulationGrid())
        pass
    
    def __setNumberToLivePlotter(self) -> None:
        self.widgets_manager.getSensorBarsPlotter().setBarsNumber( \
            self.backend_manager.getBarsNumber())
        self.widgets_manager.getFlightTestCurvesPlotter().setCurvesNumber( \
            self.backend_manager.getCurvesNumber())
        self.widgets_manager.getSimulationCurvesPlotter().setCurvesNumber( \
            self.backend_manager.getCurvesNumber())
        pass
    
    # * this function will be called in logic
    def connectBackendWithWidgets(self) -> None:
        if self.backend_manager.isBuilt() == True:
            self.__setNumberToLivePlotter()
            pass
        else:
            print("warning: MainWindowUI.BackendManager is not built")
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    @Slot()
    def __updateParametersBrowser(self) -> None:
        markdown_table: str = self.backend_manager.getLatestParametersMarkdownTable()
        self.widgets_manager.getParametersBrowser().setParametersMarkdownTable( \
            markdown_table)
        pass
    
    @Slot()
    def __updateSensorBarsPlotter(self) -> None:
        self.widgets_manager.getSensorBarsPlotter().plot( \
            self.backend_manager.getLatestSensorDataForBars())
        pass
    
    @Slot()
    def __updateFlightTestCurvesPlotter(self) -> None:
        self.widgets_manager.getFlightTestCurvesPlotter().plot( \
            self.backend_manager.getLatestTimeDataForCurves(), \
                self.backend_manager.getLatestFlightTestSensorDataForCurves())
        pass
    
    @Slot()
    def __updateSimulationCurvesPlotter(self) -> None:
        self.widgets_manager.getSimulationCurvesPlotter().plot( \
            self.backend_manager.getLatestTimeDataForCurves(), \
                self.backend_manager.getLatestSimulationSensorDataForCurves())
        pass
    
    def __updateWidgets(self) -> None:
        # ! use signal to update widgets
        self.parameters_browser_update_signal.emit()
        self.sensor_bars_plotter_update_signal.emit()
        self.flight_test_curves_plotter_update_signal.emit()
        self.simulation_curves_plotter_update_signal.emit()
        pass
    
    @noError
    @clock
    def readLatestDataAndUpdateWidgets(self, event_path: str) -> None:
        self.backend_manager.readLatestData(event_path)
        if self.backend_manager.isUpdated() == True:
            self.__updateWidgets()
            self.backend_manager.updateGrids()
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    # * this function will be called in logic
    def loadDomainsFromPath(self, data_path: str) -> None:
        relative_data_path: str = os.path.relpath(data_path, os.getcwd())
        self.backend_manager.loadDomainsFromPath(relative_data_path)
        self.__makeGridConnections()
        self.connectBackendWithWidgets()
        pass
    
    # * this function will be called in logic
    def loadMapMatrix(self, map_matrix_filename: str) -> None:
        relative_map_matrix_filename: str = \
            os.path.relpath(map_matrix_filename, os.getcwd())
        self.backend_manager.loadMapMatrix(relative_map_matrix_filename)
        self.connectBackendWithWidgets()
        pass
    
    # * this function will be called in logic
    def loadStandardModeResponse(self, standard_mode_response_filename: str) -> None:
        relative_standard_mode_response_filename: str = \
            os.path.relpath(standard_mode_response_filename, os.getcwd())
        self.backend_manager.loadStandardModeResponse(relative_standard_mode_response_filename)
        self.connectBackendWithWidgets()
        pass
    
    # * this function will be called in logic
    def loadMonitorPath(self, monitor_path: str) -> None:
        relative_monitor_path: str = os.path.relpath(monitor_path, os.getcwd())
        self.file_monitor_on_qthread.setMonitorPath(relative_monitor_path)
        pass
    
    # * this function will be called in logic
    def loadJsonFile(self, json_filename: str) -> None:
        json_filename: str = os.path.relpath(json_filename, os.getcwd())
        json_dict: dict = json.load(open(json_filename, "r", encoding=encoding))
        self.loadDomainsFromPath(json_dict["files"]["domains"])
        self.loadMapMatrix(json_dict["files"]["map matrix"])
        self.loadStandardModeResponse(json_dict["files"]["standard mode response"])
        self.loadMonitorPath(json_dict["files"]["monitor path"])
        self.backend_manager.setBasicMagnification(json_dict["settings"]["basic magnification"])
        self.backend_manager.setComparedSensorIndex( \
            json_dict["settings"]["compared sensor number"] - 1)
        self.backend_manager.setFirstColumnIndex(json_dict["settings"]["first column number"] - 1)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    # * this function will be called in logic
    def saveDataStream(self, data_stream_filename: str = "") -> None:
        save_datastream_on_qthread: CallbackOnQThread = CallbackOnQThread()
        save_datastream_on_qthread.setParent(self)
        if data_stream_filename == "":
            save_datastream_on_qthread.setCallback(lambda: \
                self.backend_manager.saveDataStream())
            pass
        else:
            data_stream_filename: str = os.path.relpath(data_stream_filename, os.getcwd())
            save_datastream_on_qthread.setCallback(lambda: \
                self.backend_manager.saveDataStream(data_stream_filename))
            pass
        save_datastream_on_qthread.setFinishedCallback(lambda: \
            saveDataStreamQMessageBox(self, data_stream_filename))
        save_datastream_on_qthread.start()
        pass
    
    # * this function will be called in logic
    def clearDataStream(self) -> None:
        self.backend_manager.clearDataStream()
        clearDataStreamQMessageBox(self)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    # * this function will be called in logic
    def startMonitoring(self) -> None:
        if self.file_monitor_on_qthread.stop_flag == False:
            alreadyMonitoringQMessageBox(self, self.file_monitor_on_qthread.monitor_path)
            pass
        else:
            self.file_monitor_on_qthread.start()
            startMonitoringQMessageBox(self, self.file_monitor_on_qthread.monitor_path)
            pass
        print("info: MainWindowUI.FileMonitorOnQThread started")
        pass
    
    # * this function will be called in logic
    def endMonitoring(self) -> None:
        self.file_monitor_on_qthread.stop()
        endMonitoringQMessageBox(self, self.file_monitor_on_qthread.monitor_path)
        print("info: MainWindowUI.FileMonitorOnQThread stopped")
        pass
    
    # * this function will be called in logic
    # * this function is updated on date: 2023-08-13
    def replayCallback(self, start_row: int, end_row: int, interval_row: int) -> None:
        if self.backend_manager.isEmpty() == True:
            pass
        else:
            main_dataframe_copy: pd.DataFrame = self.backend_manager.getMainDataFrameCopy()
            self.backend_manager.clearDataStream()
            start_row = max(start_row, 0)
            end_row = min(end_row, main_dataframe_copy.shape[0])
            n_times: int = (end_row - start_row) // interval_row
            for i_time in range(1, n_times):
                self.backend_manager.setMainDataFrame( \
                    main_dataframe_copy.iloc[start_row: start_row + i_time * interval_row, :])
                self.__updateWidgets()
                self.backend_manager.updateGrids()
                pass
            self.backend_manager.setMainDataFrame(main_dataframe_copy)
            pass
        pass
    
    # * this function will be called in logic
    # * this function is updated on date: 2023-08-13
    def replay(self, start_row: int, end_row: int, interval_row: int) -> None:
        replay_on_qthread: CallbackOnQThread = CallbackOnQThread()
        replay_on_qthread.setParent(self)
        replay_on_qthread.setCallback(lambda: \
            self.replayCallback(start_row, end_row, interval_row))
        replay_on_qthread.setFinishedCallback(lambda: replayFinishedQMessageBox(self))
        replay_on_qthread.start()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def closeEvent(self, event: QCloseEvent) -> None:
        self.widgets_manager.close()
        self.file_monitor_on_qthread.stop()
        self.backend_manager.saveDataStream()
        super().closeEvent(event)
        return
    
    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self.widgets_manager.makeSize(self.width())
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("interface: MainWindowUI.py is imported")