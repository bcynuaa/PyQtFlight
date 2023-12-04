'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-02 23:57:27
 # @ description: test for interface.MainWindowUI
 '''

from PySide2.QtWidgets import QApplication
from PySide2.QtCore import Qt

from src.interface.MainWindowUI import MainWindowUI

if __name__ == '__main__':
    # add support for high DPI display
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication([])
    main_window_ui: MainWindowUI = MainWindowUI()
    main_window_ui.show()
    main_window_ui.loadJsonFile("data//demo.json")
    main_window_ui.file_monitor_on_qthread.start()
    # main_window_ui.file_monitor_on_qthread.stop()
    app.exec_()
    pass

# expected output:

# decorator: Clock.py is imported.
# config: LanguageConfig.py is imported
# language: english, encoding: utf-8
# config path: .//config\english
# config.interface: MainWindowUIConfig is imported
# utils: FileMonitorOnQThread imported
# config.libs: PyvistaConfig.py is imported.
# config.backend: BackendManagerConfig.py is imported
# config.backend: GridsConfig.py imported
# config.backend: DomainsWithModesConfig.py is imported
# backend: DomainsWithModes is imported.
# config.backend: SensorsConfig.py is imported
# backend: Sensors.py is imported
# backend: Grids.py is imported
# config.backend: DataStreamConfig.py is imported
# utils: Paths.py is imported
# backend: DataStream is imported
# backend: BackendManager.py is imported
# config.widgets: WidgetsManagerConfig.py is imported.
# config.widgets: ParametersBrowserConfig.py is imported.
# utils: QSSModify.py is imported.
# widgets: ParametersBrowser.py is imported.
# config.widgets: CurvesPlotterConfig.py is imported.
# widget: CurvesPlotter is imported
# config.widgets: BarsPlotterConfig is imported
# widgets: BarsPlotter is imported
# config.widgets: GridPlotterConfig.py is imported.
# widgets: GridPlotter.py is imported.
# widgets: WidgetsManager is imported
# interface: MainWindowUI imported
# <src.interface.MainWindowUI.MainWindowUI(0x28d291d5130) at 0x0000028D248EFC00>
# error: Grids.allLoaded: not all loaded
# waning: BackendManager.buildBackend() failed, grids may have things not loaded
# info: domains loaded: True
# info: map matrix loaded: False
# info: standard mode response loaded: False
# warning: MainWindowUI.BackendManager is not built
# error: Grids.allLoaded: not all loaded
# waning: BackendManager.buildBackend() failed, grids may have things not loaded
# info: domains loaded: True
# info: map matrix loaded: True
# info: standard mode response loaded: False
# warning: MainWindowUI.BackendManager is not built
# BackendManager.buildBackend() succeeded
# number of sensors: 4
# number of modes: 3
# ----------------------------------------------------------------------
# error: DataStream.readLatestData(): invalid filename
# Function readLatestDataAndUpdateWidgets costs 0.0 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# error: DataStream.readLatestData(): invalid filename
# Function readLatestDataAndUpdateWidgets costs 0.0 seconds.
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# Function updateGrids costs 0.6113448143005371 seconds.
# ----------------------------------------------------------------------
# Function readLatestDataAndUpdateWidgets costs 0.676750659942627 seconds.