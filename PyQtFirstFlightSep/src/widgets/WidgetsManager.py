'''
 # @ project: PyQtFirstFlightSep
 # @ language: Python
 # @ license: Mozilla Public License 2.0
 # @ encoding: UTF-8
 # @ author: 601 | Tongqing Guo | Di Zhou | Chenyu Bao
 # @ date: 2023-08-01 17:09:49
 # @ description: widgets for WidgetsManager
 '''

import numpy as np
from PySide2.QtWidgets import QMainWindow

from src.config.libs.PyvistaConfig import *
from src.config.widgets.WidgetsManagerConfig import *

from src.widgets.ParametersBrowser import ParametersBrowser
from src.widgets.CurvesPlotter import CurvesPlotter
from src.widgets.BarsPlotter import BarsPlotter
from src.widgets.GridPlotter import GridPlotter

class WidgetsManager:
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        self.__makeCurvePlotter()
        self.__makeBarsPlotter()
        self.__makeGridPlotter()
        self.__makeParametersBrowser()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def setParent(self, parent: QMainWindow) -> None:
        # set all the widgets' parent
        self.getParametersBrowser().setParent(parent)
        self.getFlightTestCurvesPlotter().setParent(parent)
        self.getSimulationCurvesPlotter().setParent(parent)
        self.getSensorBarsPlotter().setParent(parent)
        self.getFlightTestGridPlotter().setParent(parent)
        self.getSimulationGridPlotter().setParent(parent)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __makeCurvePlotter(self) -> None:
        self.flight_test_curves_plotter_made: bool = False
        self.flight_test_curves_plotter: CurvesPlotter = CurvesPlotter()
        self.simulation_curves_plotter_made: bool = False
        self.simulation_curves_plotter: CurvesPlotter = CurvesPlotter()
        pass
    
    def __makeBarsPlotter(self) -> None:
        self.sensor_bars_plotter_made: bool = False
        self.sensor_bars_plotter: BarsPlotter = BarsPlotter()
        pass
    
    def __makeGridPlotter(self) -> None:
        self.flight_test_grid_plotter_made: bool = False
        self.flight_test_grid_plotter: GridPlotter = GridPlotter()
        self.simulation_grid_plotter_made: bool = False
        self.simulation_grid_plotter: GridPlotter = GridPlotter()
        self.flight_test_grid_plotter.setMouseReleaseEvent( \
            self.applyFlightTestCameraToSimulation)
        self.simulation_grid_plotter.setMouseReleaseEvent( \
            self.applySimulationCameraToFlightTest)
        pass
    
    def __makeParametersBrowser(self) -> None:
        self.parameters_browser: ParametersBrowser = ParametersBrowser()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def makeSize(self, total_width: float) -> None:
        parameters_browser_width, parameters_browser_height, \
            font_size, plotter_height = getSize(total_width)
        self.getParametersBrowser().setFixedSize(parameters_browser_width, parameters_browser_height)
        self.getParametersBrowser().setFontSize(font_size)
        self.getSensorBarsPlotter().setFixedHeight(plotter_height)
        self.getFlightTestCurvesPlotter().setFixedHeight(plotter_height)
        self.getSimulationCurvesPlotter().setFixedHeight(plotter_height)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def applyFlightTestCameraToSimulation(self) -> None:
        self.simulation_grid_plotter.camera = self.flight_test_grid_plotter.camera
        pass
    
    def applySimulationCameraToFlightTest(self) -> None:
        self.flight_test_grid_plotter.camera = self.simulation_grid_plotter.camera
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def getCurvesNumber(self) -> int:
        return self.flight_test_curves_plotter.n_curves
        pass
    
    def getBarsNumber(self) -> int:
        return self.sensor_bars_plotter.n_bars
        pass
    
    def getFlightTestCurvesPlotter(self) -> CurvesPlotter:
        return self.flight_test_curves_plotter
        pass
    
    def getSimulationCurvesPlotter(self) -> CurvesPlotter:
        return self.simulation_curves_plotter
        pass
    
    def getSensorBarsPlotter(self) -> BarsPlotter:
        return self.sensor_bars_plotter
        pass
    
    def getFlightTestGridPlotter(self) -> GridPlotter:
        return self.flight_test_grid_plotter
        pass
    
    def getSimulationGridPlotter(self) -> GridPlotter:
        return self.simulation_grid_plotter
        pass
    
    def getParametersBrowser(self) -> ParametersBrowser:
        return self.parameters_browser
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def connectWithFlightTestGrid(self, flight_test_grid: pyvista.UnstructuredGrid) -> None:
        self.flight_test_grid_plotter.connectWithGrid(flight_test_grid)
        self.flight_test_curves_plotter_made = True
        pass
    
    def connectWithSimulationGrid(self, simulation_grid: pyvista.UnstructuredGrid) -> None:
        self.simulation_grid_plotter.connectWithGrid(simulation_grid)
        self.simulation_curves_plotter_made = True
        pass
    
    def setCurvesNumber(self, n_curves: int) -> None:
        self.flight_test_curves_plotter.setCurvesNumber(n_curves)
        self.flight_test_curves_plotter_made = True
        self.simulation_curves_plotter.setCurvesNumber(n_curves)
        self.simulation_curves_plotter_made = True
        pass
    
    def setBarsNumber(self, n_bars: int) -> None:
        self.sensor_bars_plotter.setBarsNumber(n_bars)
        self.sensor_bars_plotter_made = True
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def setLatestFlightTestSensorDataForCurves(self, \
        time_data: np.ndarray, latest_flight_test_sensor_data) -> None:
        self.flight_test_curves_plotter.plot(time_data, latest_flight_test_sensor_data)
        pass
    
    def setLatestSimulationSensorDataForCurves(self, \
        time_data: np.ndarray, latest_simulation_sensor_data) -> None:
        self.simulation_curves_plotter.plot(time_data, latest_simulation_sensor_data)
        pass
    
    def setLatestSensorDataForBars(self, bars_amplitude: np.ndarray) -> None:
        self.sensor_bars_plotter.plot(bars_amplitude)
        pass
    
    def setLatestParametersMarkdownTable(self, markdown_table: str) -> None:
        self.parameters_browser.setParametersMarkdownTable(markdown_table)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def close(self) -> None:
        self.flight_test_grid_plotter.close()
        self.simulation_grid_plotter.close()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass

print("widgets: WidgetsManager is imported")