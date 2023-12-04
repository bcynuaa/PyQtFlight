# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 776)
        MainWindow.setStyleSheet(u"font: 11pt \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.actionLoad_Domains = QAction(MainWindow)
        self.actionLoad_Domains.setObjectName(u"actionLoad_Domains")
        self.actionLoad_Simuation_Database = QAction(MainWindow)
        self.actionLoad_Simuation_Database.setObjectName(u"actionLoad_Simuation_Database")
        self.actionLoad_Sensors_Points = QAction(MainWindow)
        self.actionLoad_Sensors_Points.setObjectName(u"actionLoad_Sensors_Points")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.left_side_vertical_layout = QVBoxLayout()
        self.left_side_vertical_layout.setObjectName(u"left_side_vertical_layout")
        self.switch_stack_list_widget_label = QLabel(self.centralwidget)
        self.switch_stack_list_widget_label.setObjectName(u"switch_stack_list_widget_label")

        self.left_side_vertical_layout.addWidget(self.switch_stack_list_widget_label)

        self.switch_stack_list_widget = QListWidget(self.centralwidget)
        self.switch_stack_list_widget.setObjectName(u"switch_stack_list_widget")

        self.left_side_vertical_layout.addWidget(self.switch_stack_list_widget)

        self.info_text_browser_label = QLabel(self.centralwidget)
        self.info_text_browser_label.setObjectName(u"info_text_browser_label")

        self.left_side_vertical_layout.addWidget(self.info_text_browser_label)

        self.info_text_browser = QTextBrowser(self.centralwidget)
        self.info_text_browser.setObjectName(u"info_text_browser")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.info_text_browser.setFont(font)

        self.left_side_vertical_layout.addWidget(self.info_text_browser)


        self.horizontalLayout_2.addLayout(self.left_side_vertical_layout)

        self.right_stacked_widget = QStackedWidget(self.centralwidget)
        self.right_stacked_widget.setObjectName(u"right_stacked_widget")
        self.main_page = QWidget()
        self.main_page.setObjectName(u"main_page")
        self.horizontalLayout = QHBoxLayout(self.main_page)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_page_flight_test_vertical_layout = QVBoxLayout()
        self.main_page_flight_test_vertical_layout.setObjectName(u"main_page_flight_test_vertical_layout")
        self.main_page_flight_test_group_box = QGroupBox(self.main_page)
        self.main_page_flight_test_group_box.setObjectName(u"main_page_flight_test_group_box")

        self.main_page_flight_test_vertical_layout.addWidget(self.main_page_flight_test_group_box)

        self.main_page_flight_test_tab_widget = QTabWidget(self.main_page)
        self.main_page_flight_test_tab_widget.setObjectName(u"main_page_flight_test_tab_widget")
        self.main_page_flight_test_time_tab = QWidget()
        self.main_page_flight_test_time_tab.setObjectName(u"main_page_flight_test_time_tab")
        self.main_page_flight_test_tab_widget.addTab(self.main_page_flight_test_time_tab, "")
        self.main_page_flight_test_frequency_tab = QWidget()
        self.main_page_flight_test_frequency_tab.setObjectName(u"main_page_flight_test_frequency_tab")
        self.main_page_flight_test_tab_widget.addTab(self.main_page_flight_test_frequency_tab, "")

        self.main_page_flight_test_vertical_layout.addWidget(self.main_page_flight_test_tab_widget)


        self.horizontalLayout.addLayout(self.main_page_flight_test_vertical_layout)

        self.main_page_simulation_vertical_layout = QVBoxLayout()
        self.main_page_simulation_vertical_layout.setObjectName(u"main_page_simulation_vertical_layout")
        self.main_page_simulation_group_box = QGroupBox(self.main_page)
        self.main_page_simulation_group_box.setObjectName(u"main_page_simulation_group_box")

        self.main_page_simulation_vertical_layout.addWidget(self.main_page_simulation_group_box)

        self.main_page_simulation_tab_widget = QTabWidget(self.main_page)
        self.main_page_simulation_tab_widget.setObjectName(u"main_page_simulation_tab_widget")
        self.main_page_simulation_time_tab = QWidget()
        self.main_page_simulation_time_tab.setObjectName(u"main_page_simulation_time_tab")
        self.main_page_simulation_tab_widget.addTab(self.main_page_simulation_time_tab, "")
        self.main_page_simulation_frequency_tab = QWidget()
        self.main_page_simulation_frequency_tab.setObjectName(u"main_page_simulation_frequency_tab")
        self.main_page_simulation_tab_widget.addTab(self.main_page_simulation_frequency_tab, "")

        self.main_page_simulation_vertical_layout.addWidget(self.main_page_simulation_tab_widget)


        self.horizontalLayout.addLayout(self.main_page_simulation_vertical_layout)

        self.right_stacked_widget.addWidget(self.main_page)
        self.signal_page = QWidget()
        self.signal_page.setObjectName(u"signal_page")
        self.right_stacked_widget.addWidget(self.signal_page)
        self.simulation_page = QWidget()
        self.simulation_page.setObjectName(u"simulation_page")
        self.right_stacked_widget.addWidget(self.simulation_page)

        self.horizontalLayout_2.addWidget(self.right_stacked_widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1200, 26))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuLoad_Data = QMenu(self.menuFile)
        self.menuLoad_Data.setObjectName(u"menuLoad_Data")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuOption = QMenu(self.menubar)
        self.menuOption.setObjectName(u"menuOption")
        self.menuTools = QMenu(self.menubar)
        self.menuTools.setObjectName(u"menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menuFile.addAction(self.menuLoad_Data.menuAction())
        self.menuLoad_Data.addAction(self.actionLoad_Domains)
        self.menuLoad_Data.addAction(self.actionLoad_Simuation_Database)
        self.menuLoad_Data.addAction(self.actionLoad_Sensors_Points)

        self.retranslateUi(MainWindow)

        self.main_page_flight_test_tab_widget.setCurrentIndex(0)
        self.main_page_simulation_tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoad_Domains.setText(QCoreApplication.translate("MainWindow", u"Load Domains", None))
        self.actionLoad_Simuation_Database.setText(QCoreApplication.translate("MainWindow", u"Load Simuation Database", None))
        self.actionLoad_Sensors_Points.setText(QCoreApplication.translate("MainWindow", u"Load Sensors Points", None))
        self.switch_stack_list_widget_label.setText(QCoreApplication.translate("MainWindow", u"\u9875\u9762\u9009\u9879\u5361", None))
        self.info_text_browser_label.setText(QCoreApplication.translate("MainWindow", u"\u4fe1\u606f\u63d0\u793a\u7a97", None))
        self.main_page_flight_test_group_box.setTitle(QCoreApplication.translate("MainWindow", u"\u8bd5\u98de3D\u6a21\u578b", None))
        self.main_page_flight_test_tab_widget.setTabText(self.main_page_flight_test_tab_widget.indexOf(self.main_page_flight_test_time_tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.main_page_flight_test_tab_widget.setTabText(self.main_page_flight_test_tab_widget.indexOf(self.main_page_flight_test_frequency_tab), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.main_page_simulation_group_box.setTitle(QCoreApplication.translate("MainWindow", u"\u4eff\u771f3D\u6a21\u578b", None))
        self.main_page_simulation_tab_widget.setTabText(self.main_page_simulation_tab_widget.indexOf(self.main_page_simulation_time_tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.main_page_simulation_tab_widget.setTabText(self.main_page_simulation_tab_widget.indexOf(self.main_page_simulation_frequency_tab), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuLoad_Data.setTitle(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuOption.setTitle(QCoreApplication.translate("MainWindow", u"Option", None))
        self.menuTools.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
    # retranslateUi

