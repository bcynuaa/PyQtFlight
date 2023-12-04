'''
 # @ coding: utf-8
 # @ language: python
 # @ project: PyQtFlightTest
 # @ author: bcynuaa
 # @ date: 2023-06-08 16:39:26
 # @ license: Mozilla Public License 2.0
 # @ description: the class of logic of main window
 '''

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from config.Name import *
from config.MainWindowSettings import *

from ui.Ui_MainWindow import Ui_MainWindow

from src.CommunicatorClass import Communicator

class MainWindow(Ui_MainWindow, QMainWindow):
    
    # ---------------------------------------------------------------------------------------------
    
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("PyQtFlightTest")
        self.communicator: Communicator = Communicator()
        self.__initializeAll()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __initializeAll(self) -> None:
        self.__initializeMenubar()
        self.__initializeTextBrowser()
        self.__initializeListWidget()
        self.__initializePyvista()
        self.__initilizeMatplotlib()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __initializeMenubar(self) -> None:
        self.__initializeMenubarFile()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __initializeMenubarFile(self) -> None:
        self.actionLoad_Domains.triggered.connect(self.__loadDomains)
        self.actionLoad_Simuation_Database.triggered.connect(self.__loadSimulationDatabase)
        self.actionLoad_Sensors_Points.triggered.connect(self.__loadSensorsPoints)
        pass
    
    def __loadDomains(self) -> None:
        data_path: str = QFileDialog.getExistingDirectory(self, \
            "选取模型数据文件路径(存有DOMAINxxx.dat)", kRelative_Path)
        try:
            self.communicator.loadDomainFilesFromPath(data_path)
            self.__writeToInfoTextBrowser( \
                "成功从路径 '" + data_path + "' 加载模型数据文件")
            self.__writeToInfoTextBrowser( \
                "模型数据文件信息\n" + self.communicator.domains_with_gen_dis.getInfo())
            pass
        except:
            QMessageBox.critical(self, \
                "错误数据路径", "路径 '" + data_path + "' 不是有效数据路径")
            pass
        pass
    
    def __loadSimulationDatabase(self) -> None:
        database_path: str = QFileDialog.getExistingDirectory(self, \
            "选取模型数据文件路径(存有SIMULATIONxxx.dat)", kRelative_Path)
        try:
            self.communicator.simulation_database.loadDatabaseFromPath(database_path)
            self.__writeToInfoTextBrowser( \
                "成功从路径 '" + database_path + "' 加载气动数据库文件")
            self.__writeToInfoTextBrowser( \
                "气动数据库文件信息\n" + self.communicator.simulation_database.getInfo())
            pass
        except:
            QMessageBox.critical(self, \
                "错误数据路径", "路径 '" + database_path + "' 不是有效数据路径")
            pass
        pass
    
    def __loadSensorsPoints(self) -> None:
        sensors_mode_dis_file, okpressed = QFileDialog.getOpenFileName(self, \
            "选取指定的传感器模态位移文件", kRelative_Path, "(*" + kData_File_Format + ")")
        if okpressed == False:
            return
        else:
            try:
                self.communicator.sensors.loadSensorsModeDisFile(sensors_mode_dis_file)
                self.__writeToInfoTextBrowser( \
                    "成功从文件 '" + sensors_mode_dis_file + "' 加载传感器模态位移数据")
                self.__writeToInfoTextBrowser( \
                    "传感器模态位移数据信息\n" + self.communicator.sensors.getInfo())
                pass
            except:
                QMessageBox.critical(self, \
                    "错误数据文件", "文件 '" + sensors_mode_dis_file + "' 不是有效数据文件")
                pass
            pass
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def __writeToInfoTextBrowser(self, message: str) -> None:
        message = kSplit_Line + "\n" + getCurrentTime() + message + "\n" + kSplit_Line
        self.info_text_browser.append(message)
        self.info_text_browser.moveCursor(self.info_text_browser.textCursor().End)
        pass
    
    def __initializeTextBrowser(self) -> None:
        self.info_text_browser.clear()
        self.info_text_browser.setMaximumWidth(kText_Browser_Width)
        self.info_text_browser.setReadOnly(True)
        self.info_text_browser.setTextColor(kQText_Browser_Font_Color)
        self.info_text_browser.setFont( \
            QFont(kQText_Browser_Font_Family, kQText_Browser_Font_Size))
        self.info_text_browser.append(kWelcome_Title)
        self.__writeToInfoTextBrowser(kWelcome_Info)
        self.info_text_browser.moveCursor(self.info_text_browser.textCursor().Start)
        pass
    
    def __initializeListWidget(self) -> None:
        # ref: 
        # - https://www.cnblogs.com/jyroy/p/9457882.html
        self.switch_stack_list_widget.setMaximumWidth(kList_View_Width)
        self.switch_stack_list_widget.setMaximumHeight(kList_View_Height)
        for key in kList_Widget_Dict:
            self.switch_stack_list_widget.insertItem(key, kList_Widget_Dict[key])
            pass
        self.switch_stack_list_widget.currentRowChanged.connect( \
            self.right_stacked_widget.setCurrentIndex)
        pass
    
    def __initializePyvista(self) -> None:
        # flight test group box
        self.main_page_flight_test_group_box.setMinimumHeight(kGroup_Box_Height)
        self.main_page_flight_test_group_box_layout = QVBoxLayout( \
            self.main_page_flight_test_group_box)
        self.main_page_flight_test_group_box_layout.addWidget( \
            self.communicator.flight_test_plotter)
        # simulation group box
        self.main_page_simulation_group_box.setMinimumHeight(kGroup_Box_Height)
        self.main_page_simulation_group_box_layout = QVBoxLayout( \
            self.main_page_simulation_group_box)
        self.main_page_simulation_group_box_layout.addWidget( \
            self.communicator.simulation_plotter)
        pass
    
    def __initilizeMatplotlib(self) -> None:
        # * flight test tabs
        self.main_page_flight_test_tab_widget.setCurrentIndex(0)
        self.main_page_flight_test_tab_widget.setMinimumHeight(kTab_Height)
        # * flight test time tab
        self.main_page_flight_test_tab_widget.setTabText(0, kTab_Name_Time_Domain)
        self.main_page_flight_test_time_domain_matplotlib_tab_layout = QVBoxLayout( \
            self.main_page_flight_test_time_tab)
        self.main_page_flight_test_time_domain_matplotlib_tab_layout.addWidget( \
            self.communicator.flight_test_time_domain_canvas.toolbar)
        self.main_page_flight_test_time_domain_matplotlib_tab_layout.addWidget( \
            self.communicator.flight_test_time_domain_canvas.canvas)
        # * flight test frequency tab
        self.main_page_flight_test_tab_widget.setTabText(1, kTab_Name_Frequency_Domain)
        self.main_page_flight_test_frequency_domain_matplotlib_tab_layout = QVBoxLayout( \
            self.main_page_flight_test_frequency_tab)
        self.main_page_flight_test_frequency_domain_matplotlib_tab_layout.addWidget( \
            self.communicator.flight_test_frequency_domain_canvas.toolbar)
        self.main_page_flight_test_frequency_domain_matplotlib_tab_layout.addWidget( \
            self.communicator.flight_test_frequency_domain_canvas.canvas)
        # * simulation tabs
        self.main_page_simulation_tab_widget.setCurrentIndex(0)
        self.main_page_simulation_tab_widget.setMinimumHeight(kTab_Height)
        # * simulation time tab
        self.main_page_simulation_tab_widget.setTabText(0, kTab_Name_Time_Domain)
        self.main_page_simulation_time_tab_layout = QVBoxLayout( \
            self.main_page_simulation_time_tab)
        self.main_page_simulation_time_tab_layout.addWidget( \
            self.communicator.simulation_time_domain_canvas.toolbar)
        self.main_page_simulation_time_tab_layout.addWidget( \
            self.communicator.simulation_time_domain_canvas.canvas)
        # * simulation frequency tab
        self.main_page_simulation_tab_widget.setTabText(1, kTab_Name_Frequency_Domain)
        self.main_page_simulation_frequency_tab_layout = QVBoxLayout( \
            self.main_page_simulation_frequency_tab)
        self.main_page_simulation_frequency_tab_layout.addWidget( \
            self.communicator.simulation_frequency_domain_canvas.toolbar)
        self.main_page_simulation_frequency_tab_layout.addWidget( \
            self.communicator.simulation_frequency_domain_canvas.canvas)
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    def closeEvent(self, event: QCloseEvent) -> None:
        # ref:
        # https://blog.csdn.net/weixin_43930603/article/details/104938939
        self.communicator.close()
        pass
    
    # ---------------------------------------------------------------------------------------------
    
    pass