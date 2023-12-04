'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-01 18:17:23
 # @ description: test for widgets.WidgetsManager
 '''

import sys
import time
from PySide2.QtGui import QCloseEvent, QResizeEvent
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget
from PySide2.QtWidgets import QHBoxLayout, QVBoxLayout
from PySide2.QtCore import Qt

from src.widgets.WidgetsManager import WidgetsManager
from src.backend.BackendManager import BackendManager

backend_manager: BackendManager = BackendManager()
data_path: str = "data//domains_data//"
map_matrix_filename: str = "data//grids_data//SensorsMap.dat"
standard_mode_response_filename: str = "data//grids_data//StandardModeResponse.dat"
latest_data_filename: str = "data//update_data//LatestData.dat"

backend_manager.loadDomainsFromPath(data_path)
backend_manager.loadMapMatrix(map_matrix_filename)
backend_manager.loadStandardModeResponse(standard_mode_response_filename)
backend_manager.buildBackend()

for i in range(100):
    backend_manager.readLatestData(latest_data_filename)
    pass

class MainWindow(QMainWindow):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("test for widgets: WidgetsManager")
        self.resize(800, 600)
        self.central_widget: QWidget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        # self.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.__makeLayout()
        self.__makeWidgetsManager()
        self.widgets_manager.makeSize(self.width())
        pass
    
    def __makeLayout(self) -> None:
        self.central_layout: QVBoxLayout = QVBoxLayout(self.central_widget)
        self.grid_plotter_layout: QHBoxLayout = QHBoxLayout()
        self.except_grid_plotter_layout: QHBoxLayout = QHBoxLayout()
        self.central_layout.addLayout(self.grid_plotter_layout)
        self.central_layout.addLayout(self.except_grid_plotter_layout)
        self.parameters_browser_layout: QVBoxLayout = QVBoxLayout()
        self.live_plotter_layout: QVBoxLayout = QVBoxLayout()
        self.except_grid_plotter_layout.addLayout(self.parameters_browser_layout)
        self.except_grid_plotter_layout.addLayout(self.live_plotter_layout)
        self.bars_plotter_layout: QHBoxLayout = QVBoxLayout()
        self.curves_plotter_layout: QHBoxLayout = QHBoxLayout()
        self.live_plotter_layout.addLayout(self.bars_plotter_layout)
        self.live_plotter_layout.addLayout(self.curves_plotter_layout)
        pass
    
    def __makeWidgetsManager(self) -> None:
        self.widgets_manager: WidgetsManager = WidgetsManager()
        self.widgets_manager.setCurvesNumber(backend_manager.getCurvesNumber())
        self.widgets_manager.setBarsNumber(backend_manager.getBarsNumber())
        self.widgets_manager.connectWithFlightTestGrid(backend_manager.getFlightTestGrid())
        self.widgets_manager.connectWithSimulationGrid(backend_manager.getSimulationGrid())
        self.__makeGridPlotterWidgets()
        self.__makeParametersBrowserWidget()
        self.__makeBarsPlotterWidget()
        self.__makeCurvesPlotterWidgets()
        pass
    
    # ! this is a important function for reference
    # def __makeSize(self) -> None:
    #     base_width: float = 100
    #     base_height: float = 100
    #     self.widgets_manager.getSensorBarsPlotter().setFixedSize(15*base_width, 2.2*base_height)
    #     self.widgets_manager.getFlightTestCurvesPlotter().setFixedSize(7.5*base_width, 2.2*base_height)
    #     self.widgets_manager.getSimulationCurvesPlotter().setFixedSize(7.5*base_width, 2.2*base_height)
    #     self.widgets_manager.getParametersBrowser().setFixedSize(4.0*base_width, 4.0*base_height)
    #     self.widgets_manager.getFlightTestGridPlotter().setFixedSize(9.5*base_width, 5.5*base_height)
    #     self.widgets_manager.getSimulationGridPlotter().setFixedSize(9.5*base_width, 5.5*base_height)
    #     pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeGridPlotterWidgets(self) -> None:
        self.grid_plotter_layout.addWidget(self.widgets_manager.getFlightTestGridPlotter())
        self.grid_plotter_layout.addWidget(self.widgets_manager.getSimulationGridPlotter())
        pass
    
    def __makeParametersBrowserWidget(self) -> None:
        self.parameters_browser_layout.addWidget(self.widgets_manager.getParametersBrowser())
        pass
        
    def __makeBarsPlotterWidget(self) -> None:
        self.bars_plotter_layout.addWidget(self.widgets_manager.getSensorBarsPlotter())
        pass
    
    def __makeCurvesPlotterWidgets(self) -> None:
        self.curves_plotter_layout.addWidget(self.widgets_manager.getFlightTestCurvesPlotter())
        self.curves_plotter_layout.addWidget(self.widgets_manager.getSimulationCurvesPlotter())
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def closeEvent(self, event: QCloseEvent) -> None:
        super().closeEvent(event)
        self.widgets_manager.close()
        pass
    
    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self.widgets_manager.makeSize(self.width())
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

if __name__ == '__main__':
    # add support for high dpi
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app: QApplication = QApplication(sys.argv)
    window: MainWindow = MainWindow()
    window.show()
    start_time: float = time.time()
    backend_manager.readLatestData(latest_data_filename)
    window.widgets_manager.setLatestParametersMarkdownTable(backend_manager.getLatestParametersMarkdownTable())
    window.widgets_manager.setLatestFlightTestSensorDataForCurves( \
        backend_manager.getLatestTimeDataForCurves(), \
            backend_manager.getLatestFlightTestSensorDataForCurves())
    window.widgets_manager.setLatestSimulationSensorDataForCurves( \
        backend_manager.getLatestTimeDataForCurves(), \
            backend_manager.getLatestSimulationSensorDataForCurves())
    window.widgets_manager.setLatestSensorDataForBars( \
        backend_manager.getLatestSensorDataForBars())
    end_time: float = time.time()
    print("time cost for one loop in backend_manager + widgets_manager except grids update: %f" % (end_time - start_time))
    window.widgets_manager.getParametersBrowser().setFontSize(15)
    sys.exit(app.exec_())
    pass

# expected output:

# config: LanguageConfig.py is imported
# language: chinese, encoding: utf-8
# config path: .//config\chinese
# config.libs: PyvistaConfig.py is imported.
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
# config.backend: BackendManagerConfig.py is imported
# decorator: Clock.py is imported.
# config.backend: GridsConfig.py imported
# config.backend: DomainsWithModesConfig.py is imported
# backend: DomainsWithModes is imported.
# config.backend: SensorsConfig.py is imported
# backend: Sensors.py is imported
# backend: Grids.py is imported
# config.backend: DataStreamConfig.py is imported
# backend: DataStream is imported
# backend: BackendManager.py is imported
# BackendManager.buildBackend() succeeded
# number of sensors: 4
# number of modes: 3
# time cost for one loop in backend_manager + widgets_manager except grids update: 0.077456