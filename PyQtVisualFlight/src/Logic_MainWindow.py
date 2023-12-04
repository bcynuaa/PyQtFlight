# coding: "utf-8"
# author: bcynuaa
# date: 2023/05/19

###################################################################################################
# This file is used to build logic in pyside2 main window

import copy

from PySide2.QtCore import *
import PySide2.QtCore
from PySide2.QtGui import *
import PySide2.QtGui
from PySide2.QtWidgets import *
import PySide2.QtWidgets

from config.Base import *
from config.ThingsInMainWindow import *
from config.PyvistaSettings import *
from config.MatplotlibSettings import *

from utils.RunBat import runBatFromAbsPath
from utils.ThreadWatchdog import Thread

from ui.Ui_MainWindow import *

from src.InteractiveClass import *

class PyQtVisualFlight(Ui_PyQtVisualFlight, QMainWindow):
    
    # ref:
    # https://blog.csdn.net/parkour_/article/details/46008807
    # which may not working
    flight_test_signal: Signal = Signal()
    simulation_signal: Signal = Signal()
    
    #------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super(PyQtVisualFlight, self).__init__()
        self.setupUi(self)
        # ! the limit time here
        self.time_limit: float = 0.
        # ! the delay time between flight test and simulation
        self.time_delay: float = 0.
        self.__initializeAll()
        pass
    
    def __initializeAll(self) -> None:
        self.flight_test_interactive: Interactive = Interactive(DEFAULT_LHS_NAME)
        self.simulation_interactive: Interactive = Interactive(DEFAULT_RHS_NAME)
        self.__initializeTrigger()
        self.__initializePyvista()
        self.__initializeMatplotlib()
        pass
    
    def __initializeTrigger(self) -> None:
        # * file trigger
        self.actionLoad_Domain_Files.triggered.connect(self.__actionLoadDomainFiles)
        self.actionFlight_Test_Observer.triggered.connect(self.__actionFlightTestObserver)
        self.actionSimulation_Observer.triggered.connect(self.__actionSimulationObserver)
        self.actionStart_Updating.triggered.connect(self.__actionStartUpdating)
        self.actionEnd_Updating.triggered.connect(self.__actionEndUpdating)
        # * option trigger
        self.actionFlight_Test_Magnification.triggered.connect(self.__actionFlightTestMagnification)
        self.actionSimulation_Magnification.triggered.connect(self.__actionSimulationMagnification)
        pass
    
    def __initializePyvista(self) -> None:
        # * flight test group box
        self.flight_test_group_box.setMinimumHeight(DEFAULT_GROUPBOX_HEIGHT)
        self.flight_test_group_box_layout = QVBoxLayout(self.flight_test_group_box)
        self.flight_test_group_box_layout.addWidget(self.flight_test_interactive.plotter_interactor)
        # * simulation group box
        self.simulation_group_box.setMinimumHeight(DEFAULT_GROUPBOX_HEIGHT)
        self.simulation_group_box_layout = QVBoxLayout(self.simulation_group_box)
        self.simulation_group_box_layout.addWidget(self.simulation_interactive.plotter_interactor)
        pass
    
    def __initializeMatplotlib(self) -> None:
        # * flight test tab widget
        self.flight_test_tab_widget.setMinimumHeight(DEFAULT_TAB_HEIGHT)
        self.flight_test_tab_widget.setCurrentIndex(0)
        # flight test time domain tab
        self.flight_test_time_domain_tab_layout = QVBoxLayout(self.flight_test_time_domain_tab)
        self.flight_test_time_domain_tab_layout.addWidget(self.flight_test_interactive.time_domain_canvas.toolbar)
        self.flight_test_time_domain_tab_layout.addWidget(self.flight_test_interactive.time_domain_canvas.canvas)
        # flight test frequency domain tab
        self.flight_test_frequency_domain_tab_layout = QVBoxLayout(self.flight_test_frequency_domain_tab)
        self.flight_test_frequency_domain_tab_layout.addWidget(self.flight_test_interactive.frequency_domain_canvas.toolbar)
        self.flight_test_frequency_domain_tab_layout.addWidget(self.flight_test_interactive.frequency_domain_canvas.canvas)
        # * simulation tab widget
        self.simulation_tab_widget.setMinimumHeight(DEFAULT_TAB_HEIGHT)
        self.flight_test_tab_widget.setCurrentIndex(0)
        # simulation time domain tab
        self.simulation_time_domain_tab_layout = QVBoxLayout(self.simulation_time_domain_tab)
        self.simulation_time_domain_tab_layout.addWidget(self.simulation_interactive.time_domain_canvas.toolbar)
        self.simulation_time_domain_tab_layout.addWidget(self.simulation_interactive.time_domain_canvas.canvas)
        # simulation frequency domain tab
        self.simulation_frequency_domain_tab_layout = QVBoxLayout(self.simulation_frequency_domain_tab)
        self.simulation_frequency_domain_tab_layout.addWidget(self.simulation_interactive.frequency_domain_canvas.toolbar)
        self.simulation_frequency_domain_tab_layout.addWidget(self.simulation_interactive.frequency_domain_canvas.canvas)
        pass
    
    #------------------------------------------------------------------------------------

    def __actionLoadDomainFiles(self) -> None:
        data_path: str = QFileDialog.getExistingDirectory(self, "选取模型数据文件路径（存有DOMAINxxx.dat）", "..//..//")
        try:
            self.flight_test_interactive.loadDomainFiles(data_path)
            self.simulation_interactive.loadDomainFiles(data_path)
            pass
        except:
            QMessageBox.critical(self, "错误数据路径", "路径" + data_path + "不是有效数据路径")
            pass
        pass
    
    def __actionFlightTestObserver(self) -> None:
        flight_test_observer_path: str = QFileDialog.getExistingDirectory(
            self, "选取飞行试验观测数据文件所在路径（存有" + observeFileName(DEFAULT_LHS_NAME) + "）",
            "..//..//"
        )
        try:
            self.flight_test_interactive.defineWatchDog(flight_test_observer_path, self.getTimeLimitForFlightTest)
            pass
        except:
            QMessageBox.critical(self, "错误数据路径", "路径" + flight_test_observer_path + "不是有效数据路径")
            pass
        pass
    
    def __actionSimulationObserver(self) -> None:
        simulation_observer_path: str = QFileDialog.getExistingDirectory(
            self, "选取仿真观测数据文件所在路径（存有" + observeFileName(DEFAULT_RHS_NAME) + "）",
            "..//..//"
        )
        try:
            self.simulation_interactive.defineWatchDog(simulation_observer_path, self.getTimeLimitForSimulation)
            pass
        except:
            QMessageBox.critical(self, "错误数据路径", "路径" + simulation_observer_path + "不是有效数据路径")
            pass
        pass
    
    def __actionStartUpdating(self) -> None:
        start_bat_file: str = QFileDialog.getOpenFileName(self, "选取启动脚本文件", "..//..//", "BAT Files (*.bat)")[0]
        self.start_bat_file: str = start_bat_file
        try:
            runBatFromAbsPath(self.start_bat_file)
            self.flight_test_thread: Thread = Thread(callbackFunction=self.flight_test_interactive.watchdog.start)
            self.simulation_thread: Thread = Thread(callbackFunction=self.simulation_interactive.watchdog.start)
            self.flight_test_thread.start()
            self.simulation_thread.start()
            self.flight_test_signal.connect(self.flight_test_thread.kill)
            self.simulation_signal.connect(self.simulation_thread.kill)
            self.flight_test_interactive.whether_in_updating = True
            self.simulation_interactive.whether_in_updating = True
        except:
            pass
        pass
    
    def __actionEndUpdating(self) -> None:
        try:
            
            self.flight_test_interactive.whether_in_updating = False
            self.simulation_interactive.whether_in_updating = False
            self.flight_test_interactive.watchdog.end()
            self.simulation_interactive.watchdog.end()
            self.flight_test_signal.emit()
            self.simulation_signal.emit()
            pass
        except:
            pass
        pass
    
    #------------------------------------------------------------------------------------
    
    def getTimeLimitForFlightTest(self) -> float:
        flight_test_total_time: float = self.flight_test_interactive.mesh.total_time
        simulation_total_time: float = self.simulation_interactive.mesh.total_time
        if self.time_limit < flight_test_total_time and self.time_limit < simulation_total_time - self.time_delay:
            self.time_limit = min(flight_test_total_time, simulation_total_time - self.time_delay)
            self.simulation_interactive.setStepByLimitTime(self.time_limit+self.time_delay)
            pass
        return self.time_limit
        pass
    
    def getTimeLimitForSimulation(self) -> float:
        flight_test_total_time: float = self.flight_test_interactive.mesh.total_time
        simulation_total_time: float = self.simulation_interactive.mesh.total_time
        if self.time_limit < flight_test_total_time and self.time_limit < simulation_total_time - self.time_delay:
            self.time_limit = min(flight_test_total_time, simulation_total_time - self.time_delay)
            self.flight_test_interactive.setStepByLimitTime(self.time_limit)
            pass
        return self.time_limit + self.time_delay
        pass
    
    #------------------------------------------------------------------------------------
    
    def __actionFlightTestMagnification(self) -> None:
        magnification, ok_pressed = QInputDialog.getDouble(
            self, "设置飞行试验位移放大倍数", "请输入飞行试验位移放大倍数",
            self.flight_test_interactive.mesh.displacement_magnification,
            decimals=4
        )
        if magnification <= 0:
            QMessageBox.warning(self, "警告", "位移放大倍数不能为零或负数")
            magnification = self.flight_test_interactive.mesh.displacement_magnification
            pass
        if ok_pressed == True:
            magnification = float(magnification)
            self.flight_test_interactive.mesh.setDisplacementMagnification(magnification)
            pass
        pass
    
    def __actionSimulationMagnification(self) -> None:
        magnification, ok_pressed = QInputDialog.getDouble(
            self, "设置仿真位移放大倍数", "请输入仿真位移放大倍数",
            self.simulation_interactive.mesh.displacement_magnification,
            decimals=4
        )
        if magnification <= 0:
            QMessageBox.warning(self, "警告", "位移放大倍数不能为零或负数")
            magnification = self.simulation_interactive.mesh.displacement_magnification
            pass
        if ok_pressed == True:
            magnification = float(magnification)
            self.simulation_interactive.mesh.setDisplacementMagnification(magnification)
            pass
        pass
    
    #------------------------------------------------------------------------------------
    
    def closeEvent(self, event: QCloseEvent) -> None:
        # ref:
        # https://blog.csdn.net/weixin_43930603/article/details/104938939
        self.flight_test_interactive.plotter_interactor.close()
        self.simulation_interactive.plotter_interactor.close()
        pass
    
    #------------------------------------------------------------------------------------
    
    pass

###################################################################################################